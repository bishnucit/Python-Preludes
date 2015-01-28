'''
Clicks on Check out and validates the next page
In the form finds the name address and email by xpath
enters values
closes the browser
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_id("wsb-button-450914890").click()
driver.find_element_by_id("wsb-button-451955160").click()
driver.find_element_by_xpath("//input[@id='email']").send_keys("example@id.com")
driver.find_element_by_xpath("//input[@id='name']").send_keys("HUMAN")
driver.find_element_by_xpath("//textarea[@id='address']").send_keys("India,EARTH")


driver.close()

