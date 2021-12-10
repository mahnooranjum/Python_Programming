# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:38:17 2020

@author: Mahnoor
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Edge(executable_path="F:/Repo/Subject_Automation/edgedriver_win64/msedgedriver.exe")

# driver = webdriver.Chrome(executable_path="F:/Repo/Subject_Automation/chromedriver_win32/chromedriver.exe")

# driver = webdriver.Ie(executable_path="F:/Repo/Subject_Automation/IEDriverServer_x64_3.150.1/IEDriverServer.exe")

driver = webdriver.Firefox(executable_path="F:/Repo/Subject_Automation/geckodriver-v0.28.0-win64/geckodriver.exe")
    


driver.get("https://en.wikipedia.org/wiki/Exile_(Taylor_Swift_song)")


print(driver.title)

print(driver.current_url)

print(driver.page_source)

print(driver.title)


driver.close()