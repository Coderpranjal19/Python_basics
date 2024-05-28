from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your chromedriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")
time.sleep(3)#to let the page refresh

search_box = driver.find_element(By.XPATH,'//input[@id="search"]')# Find the search box element
search_box.send_keys("Docker tutorial")

search_button = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']")
search_button.click()

# Close the browser
input("Press Enter to close the browser...")
driver.quit()

