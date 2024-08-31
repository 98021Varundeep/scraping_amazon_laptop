from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=XKITR2QKB0RK&sprefix=laptop%2Caps%2C818&ref=nb_sb_ss_pltr-xclick_1_6")
elem = driver.find_element(By.CLASS_NAME,"puis-card-container")

print(elem)
time.sleep(30)

driver.close()