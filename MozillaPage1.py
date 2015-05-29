from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")
driver.implicitly_wait(12)
driver.find_element_by_xpath("//*[@id='site-header']/mkt-header-child-toggle[1]").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='search-q']").send_keys("Hello")
driver.send_keys(Keys.RETURN)
assert "Hello | Firefox Marketplace" in driver.title

driver.close()
