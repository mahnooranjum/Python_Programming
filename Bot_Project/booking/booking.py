from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class Booking(webdriver.Edge):
    def __init__(self, driver_path=const.EDGE_PATH, teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown 
        os.environ['PATH']+=driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_language(self, lang = "en-us"):
        self.find_element(By.XPATH, '/html/body/header/nav[1]/div[2]/div[2]/button').click()
        self.find_element(By.CSS_SELECTOR, f'div[lang={lang}]').click()

    def change_currency(self, currency=None):
        self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]').click()
        self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]').click()

    def search_place(self, place):
        self.find_element(By.ID, 'ss').clear()
        self.find_element(By.ID, 'ss').send_keys(place)
        self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]').click()

    def select_dates(self, checkin=None, checkout=None):
        self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkin}"]').click()
        self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkout}"]').click()
    
    def select_adults(self, adults):
        self.find_element(By.ID, 'xp__guests__toggle').click()

        while True:
            self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]').click()

            if int(self.find_element(By.ID, "group_adults").get_attribute("value")) == 1:
                break

