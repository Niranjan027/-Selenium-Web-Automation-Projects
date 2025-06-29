from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(r'D:\geckodriver-v0.36.0-win64\geckodriver.exe')

driver = webdriver.Firefox(service=service)
driver.get('https://www.google.com')
print(driver.title)

driver.quit()
