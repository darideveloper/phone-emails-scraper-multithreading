import os
import re
import csv
import math
import time
import requests
import threading
from logs import logger
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv ()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
SELECTOR_EMAIL = '[href^="mailto:"]'
SELECTOR_PHONE = '[href^="tel:"]'
THREADS = int(os.getenv("THREADS", 1))
DEEP_SCRAPING = os.getenv("DEEP_SCRAPING", "").lower() == "true"
WAIT_TIME = int(os.getenv("WAIT_TIME", 0))
CSV_INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.csv")
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

def get_subpages (soup:BeautifulSoup, page:str):
    """ Get all subpages in the current page

    Args:
        soup (BeautifulSoup): bs4 instance of the current page
        page (str): link of the current page

    Returns:
        list: list of subpages (included the current page)
    """
    
    if page.endswith("/"):
        page = page[:-1]
    
    # Get comain of current page
    domain = page.replace("http://", "").replace("https://", "").split("/")[0]
    
    # Get all links in page
    # selector_links = f'[href~="{domain}"]' 
    selector_links = f'[href]:not({SELECTOR_EMAIL}):not({SELECTOR_PHONE}):not([href="#"])' 
    links_elems = soup.select(selector_links)
    links = list(map(lambda link: f'{page}{link["href"].replace("//", "")}' if "www" in link or "http" in link else link["href"], soup.select(selector_links)))
    
    # Filter links to get only subpages
    suffixes = ("/", ".html", ".php")
    links_subpages = set(filter(lambda page: domain in page and (
        page.endswith("/") or
        page.endswith(".com") or
        page.endswith(".org") or
        page.endswith(".php") or
        page.endswith(".html")         
        ), links))
    
    # Add original page to subpages
    if not page in links_subpages:
        links_subpages.add (page)
    
    # Format links
    links_subpages = set (map(lambda page: page if page.endswith("/") else page+"/", links_subpages))
    
    return list(links_subpages)
    
def get_soup (page:str, thread_num:int):
    """ Get the bs4 instance of a page

    Args:
        page (str): link of the page

    Returns:
        BeautifulSoup: bs4 instance of the page
    """
    
    page = page.strip()
    if not "http" in page:
        page = "https://" + page
        
    try:
        time.sleep(WAIT_TIME)
        res = requests.get(page, headers=HEADERS)
    except Exception as err:
        # Skipo to next page
        return None
    
    res_text_formated = res.text.replace("<", "\n<")
    
    # Parse page to bs4
    if res.status_code != 200:
        logger.warning (f"(thread {thread_num})     Page don't work: " + page)
        return None
    
    soup = BeautifulSoup(res_text_formated, "html.parser")
    
    return soup

def scrape_pages (pages:list, thread_num:int, data:list):
    """ Extract data from specific pages in a thread

    Args:
        pages (list): list of pages to scrape
        thread_num (int): number of the current thread
        data (list): list where data will be saved
    """
    
    # Loop through csv rows
    for page in pages:
        
        if not "https" in page:
            page = "https://" + page
        
        page = page.replace("\n", "")
        
        logger.info (f"(thread {thread_num})   scanning subpages of {page}")
        
        # Get bs4 instance
        soup = get_soup (page, thread_num)
        if not soup:
            continue
        
        # Get subpages in current page
        subpages = get_subpages (soup, page)
        
        emails = []
        phones = []
        for subpage in subpages:
            
            soup = get_soup (subpage, thread_num)
            
            # Skip for request if page don't work
            if soup:
                
                logger.info (f"(thread {thread_num}) Scraping page: {subpage}")
                    
                # Get phone and email with requests selectors
                emails += list(map(lambda email: email["href"], soup.select(SELECTOR_EMAIL)))
                phones += list(map(lambda phone: phone["href"], soup.select(SELECTOR_PHONE)))    
                
                # Get phone and email with regex if there are not found with css selectors
                body = soup.find("body")
                
                if not body:
                    continue
                
                body_text = body.getText()
                emails_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
                emails += re.findall(emails_regex, body_text)
                phone_regex = re.compile(r"(\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{3}[\s.-]?\d{4})")
                phones += re.findall(phone_regex, body_text)
            
            # Format emails and phones using function and removing empty values
            emails = list(set(filter(lambda email: email, map(format_email, set(emails)))))
            phones = list(set(filter(lambda phone: phone, map(format_phone, set(phones)))))
            
            # End loop if emails and phones are found, when DEEP_SCRAPING is false
            if emails and phones and not DEEP_SCRAPING:
                break
            
        # Save found data
        data.append ([page, " ".join(emails), " ".join(phones)])
    

def main (): 
    """ Scrape pages from "input.csv" file and save results to "output.csv" file """
    
    # Validate input file
    if not os.path.isfile(CSV_INPUT_PATH):
        logger.info ("File 'input.csv' not found")
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