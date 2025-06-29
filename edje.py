from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
service = Service(r'D:\edgedriver_win64\msedgedriver.exe')
options = Options()
options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
driver = webdriver.Edge(service=service, options=options)
driver.get('https://www.google.com')
print(driver.title)

driver.quit()
