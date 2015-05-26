from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")

driver.find_element_by_link_text('Popular').click()
assert "Popular | Firefox Marketplace" in driver.title


driver.find_elements_by_css_selector(a:contains('spicy-cookie-6')).click()
driver.find.send_keys(Keys.RETURN)

driver.find_elements_by_css_selector(a:contains('Load more')).click()
assert "loadmore loading" in driver.page_source


driver.find_element_by_xpath("//input[@name='email']").send_keys('bishnucit@gmail.com')
driver.find_elements_by_css_selector(a:contains('Sign me up')).click()
assert "privacy" in driver.page_source
driver.find_element_by_xpath("//input[@name='privacy']").click()
driver.find_elements_by_css_selector(a:contains('Sign me up')).click()


assert "success" in driver.page_source



driver.close()
