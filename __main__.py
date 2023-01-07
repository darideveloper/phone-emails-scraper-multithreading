import os
import re
import csv
import requests
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
    
def main (): 
    """ Scrape pages from "pages.csv" file and save results to "output.csv" file """
    
    # Start scraper
    scraper = None
    if USE_SELENIUM:
        scraper = Web_scraping(headless=True)
    
    # csv paths
    csv_input_path = os.path.join(os.path.dirname(__file__), "pages.csv")
    csv_output_path = os.path.join(os.path.dirname(__file__), "output.csv")
    
    # Validate input file
    if not os.path.isfile(csv_input_path):
        print ("File 'pages.csv' not found")
        return ""
    
    # Read csv file content
    with open (csv_input_path, "r") as file:
        pages = set(file.readlines())
        
    # TODO: split pages in chunks to allow multiprocessing
        
    # Loop through csv rows
    data = [["page", "emails", "phones"]]
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
        
        # Parse page to bs4
        if res.status_code != 200:
            print ("Error scraping page: " + page)
            continue
        print ("Scraping page: " + page)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Get phone and email with requests selectors
        emails = list(map(lambda email: email["href"], soup.select(SELECTOR_EMAIL)))
        phones = list(map(lambda phone: phone["href"], soup.select(SELECTOR_PHONE)))    
        
        # Get phone and email with regex if there are not found with css selectors
        body_text = soup.get_text()
        emails_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        emails += re.findall(emails_regex, body_text)
        phone_regex = re.compile(r"(\+?\d{1,3}[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{3}[\s.-]?\d{4})")
        phones += re.findall(phone_regex, body_text)
        
        # Get phone and email with selenium if there are not found with regex
        if scraper and (not emails or not phones):
            scraper.set_page(page)
            emails += scraper.get_attribs(SELECTOR_EMAIL, "href")
            phones += scraper.get_attribs(SELECTOR_PHONE, "href")
        
        # Format emails and phones
        emails = set(map(format_email, set(emails)))
        phones = set(map(format_phone, set(phones)))
        
        # Save found data
        data.append ([page, " ".join(emails), " ".join(phones)])

    # Save data to csv file when finished
    with open (csv_output_path, "w", encoding='UTF-8', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    main()