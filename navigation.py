import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service = Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(2)
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("EuroTruck simulator 2")
search_box.send_keys(Keys.RETURN)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(3)
print("successfully clicked")
driver.quit()