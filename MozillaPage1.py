from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")
driver.find_element_by_class_name("header--search-togle").click()
driver.implicitly_wait(2)
driver.find_element_by_id("search-q").send_keys("Hello")
driver.find.send_keys(Keys.RETURN)
assert "Hello | Firefox Marketplace" in driver.title

driver.close()
