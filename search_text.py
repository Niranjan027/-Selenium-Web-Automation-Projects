from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
browser.get("https://www.google.com/")
browser.maximize_window()

search_box = browser.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN) 
print("Search completed.")
time.sleep(9)
browser.quit()