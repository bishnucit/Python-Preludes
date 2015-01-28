from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_link_text("Check Out").click()
assert "Check Out" in driver.title
driver.close()