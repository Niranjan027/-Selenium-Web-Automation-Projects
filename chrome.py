from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')
search_box = driver.find_elements(By.NAME, "q")
search_box.send_keys("selenium")
print(driver.title)

driver.quit()
