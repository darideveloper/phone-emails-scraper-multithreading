import os
import csv
from scraping_manager.automate import Web_scraping

def main (): 
    # csv path
    csv_path = os.path.join(os.path.dirname(__file__), "pages.csv")
    if not os.path.isfile(csv_path):
        print ("File 'pages.csv' not found")
        return ""
    
    # Read csv file content
    with open (csv_path, "r") as file:
        pages = file.readlines()
        
    # Loop through csv rows
    for page in pages:
        
        page = page.strip()
        
        print (page)


if __name__ == "__main__":
    main()