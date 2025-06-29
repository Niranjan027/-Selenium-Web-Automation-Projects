from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://practice.expandtesting.com/checkboxes')
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='checkbox1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='checkbox1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='checkbox2']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='checkbox2']").click()
time.sleep(5)
driver.quit() 