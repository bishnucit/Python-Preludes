from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#opening the webpage
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
assert "Welcome" in driver.title
print ("success")
driver.close()