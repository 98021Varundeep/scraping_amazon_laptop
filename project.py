from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file_no = 1

for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=XKITR2QKB0RK&qid=1725095124&sprefix=laptop%2Caps%2C818&ref=sr_pg_2")
    
    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)} items found")
    for  elem in elems:
        d= elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file_no}.html","w", encoding = "utf-8") as f:
            f.write(d)
            file_no += 1
    #print(elem.text)
    time.sleep(8)

driver.close()