from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\Trojan\Desktop\Selenium\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.wscubetech.com/")

driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div[2]/div")
driver.find_element(By.XPATH, "/html/body/section[4]")

breakpoint()
