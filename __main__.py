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
    with open (csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        csv_rows = set(list(csv_reader))
        
    # Loop through csv rows
    for (page, ) in csv_rows:
        print (page)


if __name__ == "__main__":
    main()