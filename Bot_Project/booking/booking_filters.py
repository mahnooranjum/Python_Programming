
from re import L

from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFilters():
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def apply_star(self, *stars):
        ele = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        eles= ele.find_elements(By.CSS_SELECTOR, "*")

        for val in stars:
            for e in eles:
                if str(e.get_attribute('innerHTML')).strip() == f'{val} stars':
                    e.click()

    def sort_by_lowest(self):
        self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]').click()


