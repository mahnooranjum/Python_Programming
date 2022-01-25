
from selenium import webdriver
import os 

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge("E:/WorkFiles/Github/Python_Programming/Subject_Automation/seleniumDrivers/msedgedriver")

driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
ele = driver.find_element_by_id('downloadButton')
ele.click()



WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        #filter
        (By.CLASS_NAME, 'progress-label'),
        'Complete!' 
        #text
    )
)

prog_ele = driver.find_elements_by_class_name('progress-label')
print(prog_ele)