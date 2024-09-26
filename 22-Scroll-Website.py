from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/Trojan/Desktop/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")

time.sleep(5)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
