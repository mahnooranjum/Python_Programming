
from selenium import webdriver
import os 

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge("E:/WorkFiles/Github/Python_Programming/Subject_Automation/seleniumDrivers/msedgedriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(20)

try:
    ele = driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-button-holder"]/a[2]')
    ele.click()
except:
    print('no element with this class')

el1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')
el2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')

el1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
el2.send_keys(Keys.NUMPAD3, Keys.NUMPAD5)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button').click()
# driver.find_element_by_css_selector('button[onclick="return total()"').click()

while len(driver.find_element_by_id('displayvalue').text)==0:
    pass


print(driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div/span').text)