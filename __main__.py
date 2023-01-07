import os
import re
import csv
import math
import requests
import threading
from logs import logger
from time import sleep
from bs4 import BeautifulSoup
from scraping_manager.automate import Web_scraping
from dotenv import load_dotenv

load_dotenv ()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
SELECTOR_EMAIL = '[href^="mailto:"]'
SELECTOR_PHONE = '[href^="tel:"]'
USE_SELENIUM = os.getenv("USE_SELENIUM", "").lower() == "true"
THREADS = int(os.getenv("THREADS", 1))
CSV_INPUT_PATH = os.path.join(os.path.dirname(__file__), "pages.csv")
CSV_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "output.csv")

def format_email (email:str):
    """ Format email address, removing extra words """
    
    email = email.replace("mailto:", "")
    
    email_words = email.split(" ")
    for word in email_words:
        if "@" in word:
            return word
        
def format_phone (phone:str):
    """ Clean phone number, removing extra characters """
    
    phone = phone.replace("tel:", "")

    clean_phone = ""
    for char in str(phone):
        if char.isnumeric():
            clean_phone += char
    return clean_phone

def split (pages, threads):
    chunk_size = math.ceil(len(pages) / threads)
    for start in range(0, len(pages), chunk_size):
        yield pages[start:start + chunk_size]

def scrape_pages (pages, thread_num, data):
    
    # Start scraper
    scraper = None
    if USE_SELENIUM:
        logger.info (f"(thread {thread_num}) chrome started in background")
        scraper = Web_scraping(headless=True)
    
    # Loop through csv rows
    for page in pages:
        
        # Format page
        page = page.strip()
        if not "http" in page:
            page = "https://" + page
            
        try:
            res = requests.get(page, headers=HEADERS)
        except Exception as err:
            # Skipo to next page
            continue
        
        res_text_formated = res.text.replace("<", "\n<")
        
        # Parse page to bs4
        if res.status_code != 200:
            logger.warning (f"(thread {thread_num}) Page don't work: " + page)
            continue
        logger.info (f"(thread {thread_num}) Scraping page: " + page)
        soup = BeautifulSoup(res_text_formated, "html.parser")
        
        # Get phone and email with requests selectors
        emails = list(map(lambda email: email["href"], soup.select(SELECTOR_EMAIL)))
        phones = list(map(lambda phone: phone["href"], soup.select(SELECTOR_PHONE)))    
        
        # Get phone and email with regex if there are not found with css selectors
        body_text = soup.find("body").getText()
        emails_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        emails += re.findall(emails_regex, body_text)
        phone_regex = re.compile(r"(\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{3}[\s.-]?\d{4})")
        phones += re.findall(phone_regex, body_text)
        
        # Get phone and email with selenium if there are not found with regex
        if scraper and (not emails or not phones):
            scraper.set_page(page)
            emails += scraper.get_attribs(SELECTOR_EMAIL, "href")
            phones += scraper.get_attribs(SELECTOR_PHONE, "href")
        
        # Format emails and phones using function and removing empty values
        emails = set(filter(lambda email: email, map(format_email, set(emails))))
        phones = set(filter(lambda phone: phone, map(format_phone, set(phones))))
        
        # Save found data
        data.append ([page, " ".join(emails), " ".join(phones)])
    

def main (): 
    """ Scrape pages from "pages.csv" file and save results to "output.csv" file """
    
    # Validate input file
    if not os.path.isfile(CSV_INPUT_PATH):
        logger.info ("File 'pages.csv' not found")
        return ""
    
    # Read csv file content
    with open (CSV_INPUT_PATH, "r") as file:
        pages = list(set(file.readlines()))
    
    # Create threads
    data = [["page", "emails", "phones"]]
    pages_threads = list(split(pages, THREADS))
    threads_objs = []
    for pages_thread in pages_threads:
        sleep (0.1)
        index = pages_threads.index(pages_thread) + 1
        logger.info ("Starting thread " + str(index) + " of " + str(len(pages_threads)))
        thread_obj = threading.Thread(target=scrape_pages, args=(pages_thread, index, data))
        thread_obj.start ()
        threads_objs.append (thread_obj)
        
    # Wait for threads to finish
    while True:
        sleep (1)
        running_threads = list(filter (lambda thread: thread.is_alive(), threads_objs))
        if not running_threads:
            break
        
    # Save data to csv file when finished
    with open (CSV_OUTPUT_PATH, "w", encoding='UTF-8', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    

if __name__ == "__main__":
    main()