import os
import csv
import requests
from bs4 import BeautifulSoup
from scraping_manager.automate import Web_scraping

def main (): 
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
        print ()
        


if __name__ == "__main__":
    main()