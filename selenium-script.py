from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
from datetime import datetime, timedelta

# Specify the date range
start_date = '2022-01-01'
end_date = '2022-01-02'

# Convert to datetime objects
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

# Initialize the WebDriver
PATH = "D:\\chromium\\chromedriver"
driver = webdriver.Chrome(PATH)

# Open the CSV file for writing
with open('kalimati_arrivals.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    header_text = ["Date", "Commodity", "Unit", "Arrival" ]
    csv_writer.writerow(header_text)

    current_date = start_date
    while current_date <= end_date:
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')
        
        try:
            # Navigate to the website
            driver.get("https://kalimatimarket.gov.np/lang/en")
            driver.get("https://kalimatimarket.gov.np/daily-arrivals")
            
            # Find the date input field
            search = driver.find_element_by_id('datePricing')

            # Enter the date
            search.clear()  # Clear any existing text in the input field
            search.send_keys(year)
            search.send_keys(Keys.ARROW_RIGHT)
            search.send_keys(month)
            search.send_keys(Keys.ARROW_RIGHT)
            search.send_keys(day)
            search.send_keys(Keys.RETURN)
            
            time.sleep(1)

            selected_date = current_date.strftime('%Y-%m-%d')

            # Find the table
            table = driver.find_element_by_id('commodityPriceParticular')
            rows = table.find_elements_by_tag_name("tr")


            # Loop through rows (skip header if written)
            for row in rows[1:]:
                cells = row.find_elements_by_tag_name("td")
                cell_text = [selected_date] + [cell.text for cell in cells]
                csv_writer.writerow(cell_text)

        except Exception as e:
            print(f"Error processing date {current_date}: {e}")
        
        # Move to the next day
        current_date += timedelta(days=1)

driver.quit()
