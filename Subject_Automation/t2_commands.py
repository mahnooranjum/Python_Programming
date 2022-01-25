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

driver = webdriver.Firefox(executable_path="/geckodriver-v0.28.0-win64/geckodriver.exe")
    


driver.get("http://demo.automationtesting.in/Windows.html")


print(driver.title)

print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(2)

#driver.close()
driver.quit()