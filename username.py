from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/login")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("niranjang.it2022@citchennai.net")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Nira@2004")
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print("Login attempted. Check if login was successful.")
    time.sleep(10)

finally:
    driver.quit()
