'''
If you are using Python 2.7 instead of 3 please remove the brackets from print statement.
the last select code is very tricky understand it before coding.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/check-out.html")
# driver.find_element_by_id("wsb-button-450914890").click()
# driver.find_element_by_id("wsb-button-451955160").click()

driver.find_element_by_xpath("//input[@id='email']").send_keys("example@id.com")
driver.find_element_by_xpath("//input[@id='name']").send_keys("HUMAN")
driver.find_element_by_xpath("//textarea[@id='address']").send_keys("India,EARTH")
driver.find_element_by_xpath("//select[@id='card_type']/option[3]").click()
driver.find_element_by_css_selector("div.form-actions > button").click()

assert "Menu"  in driver.title
print ("Success, You have done it. All validation completed!! Congratulations")
driver.close()

