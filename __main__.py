import os
import csv
import requests
from bs4 import BeautifulSoup
from scraping_manager.automate import Web_scraping

def format_email (email:str):
    """ Format email address, removing extra words """
    email_words = email.split(" ")
    for word in email_words:
        if "@" in word:
            return word
        
def format_phone (phone:str):
    """ Clean phone number, removing extra characters """

    clean_phone = ""
    for char in str(phone):
        if char.isnumeric():
            clean_phone += char
    return clean_phone
    

def main (): 
    """ Scrape pages from "pages.csv" file and save results to "output.csv" file """
    
    # csv path
    csv_path = os.path.join(os.path.dirname(__file__), "pages.csv")
    if not os.path.isfile(csv_path):
        print ("File 'pages.csv' not found")
        return ""
    
    # Read csv file content
    with open (csv_path, "r") as file:
        pages = set(file.readlines())
        
    # Loop through csv rows
    for page in pages:
        
        # Format page
        page = page.strip()
        if not page.startswith("http"):
            page = "https://" + page
            
        # variables for storage results
        found_emails = []
        found_phones = []
            
        # Scrape page with requests and parse to soup
        res = requests.get(page)
        if res.status_code != 200:
            print ("Error scraping page: " + page)
            continue
        print ("Scraping page: " + page)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Get phone and email with css selectors
        found_emails += list(map(lambda email: email.get_text(), soup.select('[href^="mailto:"]')))
        found_phones += list(map(lambda phone: phone.get_text(), soup.select('[href^="tel:"]')))
        
        # Clean scraped data
        found_emails = list(map(format_email, found_emails))
        found_phones = list(map(format_phone, found_phones))
        
        # TODO: Get phone and email with regex
        
        # TODO: Get phone and email with selenium
        
        print ()

if __name__ == "__main__":
    main()