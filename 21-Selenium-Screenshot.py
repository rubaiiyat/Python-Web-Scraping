from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(r"C:\Users\Trojan\Desktop\Selenium\chromedriver.exe")

driver = webdriver.Chrome(service=s)


driver.get("https://www.google.com/")

search = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"
)

time.sleep(2)
search.send_keys("youtube")

search.send_keys(Keys.ENTER)

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "youtube").click()


time.sleep(2)

driver.save_screenshot("C:/Users/Trojan/Documents/Lightshot/youtube.png")
