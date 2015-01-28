from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_link_text("Our Passion").click()
assert "Our Passion" in driver.title
driver.close()