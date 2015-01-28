'''
Clicks on Check out and validates the next page
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_id("wsb-button-450914890").click()
driver.find_element_by_id("wsb-button-451955160").click()

assert "Check Out" in driver.title
driver.close()

