from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    print(url, "hello")
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Set up the WebDriver
    service = Service('/usr/local/bin/chromedriver')  # Adjust the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to the URL
    driver.get(url)
    
    # Wait for JavaScript to load
    time.sleep(5)  # Adjust the sleep time as needed
    
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    text = soup.get_text(separator='\n')
    
    # Close the WebDriver
    driver.quit()
    
    return text