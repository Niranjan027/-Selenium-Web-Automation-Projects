from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.expandtesting.com/dropdown")
time.sleep(3)
dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)

select.select_by_visible_text("Option 2")
time.sleep(3)

select.select_by_index(1)
time.sleep(2)

select.select_by_value("2")
time.sleep(2)

option_count = len(select.options)
expected_count = 3
if option_count == expected_count:
    print("Test case passed. Count is correct.")
else:
    print("Test case failed. Count is incorrect.")

target_value = "Option 2"
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option: {target_value}")
        break
else:
    print(f"Option '{target_value}' not found")

time.sleep(3)
driver.quit()
