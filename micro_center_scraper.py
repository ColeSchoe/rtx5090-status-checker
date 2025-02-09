import csv, os, time, datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RTX5090Listing import RTX5090Listing

rtx_5090_page_microcenter = "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937+4294802166+4294802144&myStore=true"

def searchThroughMicroCenter(url, csv_file):
    page = webdriver.Chrome()

    while(True):
        page.get(url)

        # Sleep for a bit to avoid bot detection
        time.sleep(randint(3,10))
        
        unfiltered_listings = page.find_elements(By.CLASS_NAME, "details")
        number_of_listings = unfiltered_listings.__len__()
        current_listing = 0
        while current_listing < number_of_listings:
            current_5090 = RTX5090Listing()

            # Finding the product name
            product_name = page.find_elements(By.CLASS_NAME, "productClickItemV2")[current_listing].get_attribute("data-name")
            product_brand = page.find_elements(By.CLASS_NAME, "productClickItemV2")[current_listing].get_attribute("data-brand")
            current_5090.product_name = product_brand + " " + product_name

            # Finding the product price
            try:
                price_element = page.find_elements(By.CSS_SELECTOR, "div.price")[current_listing].text
                index = price_element.__len__()-1
                while (price_element[index] != "$"):
                    index -= 1

                current_5090.price = price_element[index:]
            except (Exception):
                break

            # Finding the stock and availability of the product
            try:
                stock_element = page.find_elements(By.CSS_SELECTOR, "div.stock")[current_listing].text
                if "SOLD OUT" in stock_element:
                    current_5090.no_units = 0
                    current_5090.available = False
                else:
                    current_5090.no_units = "In-store pickup only"
                    current_5090.available = True
                
            except (Exception):
                stock_element = page.find_elements(By.CSS_SELECTOR, "div.stock")[-1].text
                if "SOLD OUT" in stock_element:
                    current_5090.no_units = 0
                    current_5090.available = False
                else:
                    current_5090.no_units = "In-store pickup only"
                    current_5090.available = True
            
            # Link to product page
            link_element = page.find_elements(By.CLASS_NAME, "productClickItemV2")[current_listing].get_attribute("href")
            current_5090.link = link_element

            # Location and time found information
            current_5090.store = "Micro Center"
            current_5090.time = datetime.datetime.now()

            with open(csv_file, "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([current_5090.product_name, current_5090.price, current_5090.available, current_5090.no_units, current_5090.store, current_5090.time, current_5090.link])

            current_listing += 1
        break

    return


if __name__ == "__main__":
    csv_file = "microcenterdata.csv"

    # Opening a file to put quotes in csv form, creating it if it doesn't already exist
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Available", "No. Units", "Store", "Time", "Link"])
    
    # Search through Micro Center's site for information on 5090 listings
    searchThroughMicroCenter(rtx_5090_page_microcenter, csv_file)