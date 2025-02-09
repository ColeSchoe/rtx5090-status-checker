import csv, os, time, datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from RTX5090Listing import RTX5090Listing
from send_email import send_message

rtx_5090_best_buy_page = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=abcat0507002&id=pcat17071&iht=n&ks=960&list=y&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~Nvidia%20GeForce%20RTX%205090&sc=Global&st=categoryid%24abcat0507002&type=page&usc=All%20Categories"

def searchThroughBestBuy(url, csv_file):
    page = webdriver.Chrome()

    while(True):
        page.get(url)

        # Sleep for a bit to avoid bot detection
        time.sleep(randint(3,10))

        unfiltered_listings = page.find_elements(By.CLASS_NAME, "sku-item")
        number_of_listings = unfiltered_listings.__len__()
        current_listing = 0
        while current_listing < number_of_listings:
            current_5090 = RTX5090Listing()

            # Finding the product name
            try:
                product_name = page.find_elements(By.CSS_SELECTOR, "h4.sku-title")[current_listing].text
                current_5090.product_name = product_name
            except (Exception):
                break

            # Finding the product price
            try:
                price_element = page.find_elements(By.CSS_SELECTOR, "span.sr-only")[current_listing].text
                index = price_element.__len__()-1
                while (price_element[index] != "$"):
                    index -= 1
                current_5090.price = price_element[index:]
            except (Exception):
                break

            # Finding the stock and availability of the product
            try:
                stock_element = page.find_elements(By.CSS_SELECTOR, "div.fulfillment-fulfillment-summary")[current_listing].text
                if "Sold Out" in stock_element:
                    current_5090.no_units = 0
                    current_5090.available = False
                else:
                    current_5090.no_units = "In-store pickup only"
                    current_5090.available = True
                
            except (Exception):
                stock_element = page.find_elements(By.CSS_SELECTOR, "div.fulfillment-fulfillment-summary")[-1].text
                if "Sold Out" in stock_element:
                    current_5090.no_units = 0
                    current_5090.available = False
                else:
                    current_5090.no_units = "?"
                    current_5090.available = True
            
            # Link to product page
            link_element = page.find_elements(By.CSS_SELECTOR, "a.image-link")[current_listing].get_attribute("href")
            current_5090.link = link_element

            # Location and time found information
            current_5090.store = "Best Buy"
            current_5090.time = datetime.datetime.now()

            # Send email showing availability and a link to the product
            if (current_5090.available):
                send_message("5090 Available at: ", current_5090.link)

            # Log data
            with open(csv_file, "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([current_5090.product_name, current_5090.price, current_5090.available, current_5090.no_units, current_5090.store, current_5090.time, current_5090.link])

            current_listing += 1
        break

    return


if __name__ == "__main__":
    csv_file = "bestbuydata.csv"

    # Opening a file to put quotes in csv form, creating it if it doesn't already exist
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Available", "No. Units", "Store", "Time", "Link"])
    
    # Search through Newegg's site for information on 5090 listings
    searchThroughBestBuy(rtx_5090_best_buy_page, csv_file)