'''
Clicks on Herbal tea collection
checks for the page title 
validates
closes the browser
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_id("wsb-button-450914890").click()
assert "Menu" in driver.title
driver.close()

