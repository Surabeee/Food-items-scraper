from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# This script uses Selenium to scrape the food menu and price details from a Magicpin restaurant page called chinese Dhaba.

options = Options()
options.headless = True  # Run in headless mode
service = Service("C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Update this with the path to your ChromeDriver

driver = webdriver.Chrome(service=service, options=options)

# URL of the Magicpin restaurant page
url = 'https://magicpin.in/New-Delhi/Sunehri-Bagh-Road-Area/Restaurant/Chinese-Dhaaba/store/43ba2b/delivery/'

driver.get(url)

wait = WebDriverWait(driver, 10)
menu_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'catalogItemsHolder')))

# This part handles clicking on any "show more" buttons to ensure all menu items are visible.
hidden_sections = driver.find_elements(By.XPATH, "//div[contains(@class, 'catalogItemsHolder')]//button[contains(@class, 'show-more')]")
for section in hidden_sections:
    driver.execute_script("arguments[0].click();", section)
    time.sleep(2)  

soup = BeautifulSoup(driver.page_source, 'html.parser')


menu_items = soup.find_all('section', class_='categoryItemHolder')

menu_details = []
for item in menu_items:
    name = item.find('p', class_='itemName').get_text(strip=True)
    price = item.find('span', class_='itemPrice').get_text(strip=True)
    menu_details.append({'name': name, 'price': price})

# The menu details are printed with numbering using the enumerate function.
for idx, detail in enumerate(menu_details, start=1):
    print(f"{idx}. Name: {detail['name']}, Price: {detail['price']}")

driver.quit()
