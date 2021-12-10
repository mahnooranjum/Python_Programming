# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:06:01 2020

@author: Mahnoor
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Edge(executable_path="F:/Repo/Subject_Automation/edgedriver_win64/msedgedriver.exe")

# driver = webdriver.Chrome(executable_path="F:/Repo/Subject_Automation/chromedriver_win32/chromedriver.exe")

# driver = webdriver.Ie(executable_path="F:/Repo/Subject_Automation/IEDriverServer_x64_3.150.1/IEDriverServer.exe")

driver = webdriver.Firefox(executable_path="F:/Repo/Subject_Automation/geckodriver-v0.28.0-win64/geckodriver.exe")
    


driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(1)
print(driver.title)

driver.get("https://en.wikipedia.org/wiki/Exile_(Taylor_Swift_song)")
time.sleep(1)
print(driver.title)

driver.back()
time.sleep(1)
print(driver.title)

driver.forward()
time.sleep(1)
print(driver.title)

driver.back()
time.sleep(1)
print(driver.title)

#driver.close()
driver.quit()