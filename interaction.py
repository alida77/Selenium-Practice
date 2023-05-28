from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:/Users/alih/OneDrive/Documents/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_in_english = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
articles_in_english.click()
print(articles_in_english.text)

x = driver.find_element(By.NAME)
x.send_keys()