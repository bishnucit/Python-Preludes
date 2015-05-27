from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")

assert "Develop Apps" in driver.page_source
driver.find_element_by_link_text('/developers/').click()
assert "Developers | Firefox Marketplace" in driver.title


assert "API Reference" in driver.page_source
driver.find_element_by_css_selector('.devhub-links > a:nth-child(1)').click()
assert "App Development API Reference - App Center | MDN" in driver.title
driver.back()

assert "Support" in driver.page_source
driver.find_element_by_css_selector('.devhub-links > a:nth-child(2)').click()
assert "Support | Developers | Firefox Marketplace" in driver.title
driver.back()

assert "Submit an app" in driver.page_source
driver.find_element_by_css_selector('a.submit:nth-child(3)').click()
assert "Sign in / Sign up" in driver.page_source
driver.back()

assert "My Submissions" in driver.page_source
driver.find_element_by_css_selector('.devhub-links > a:nth-child(4)').click()
assert "proceed" in driver.page_source
driver.back()

assert "Marketplace" in driver.page_source
driver.find_element_by_css_selector('a.submit:nth-child(5)').click()
assert "Firefox Marketplace" in driver.title
driver.back()


driver.close()
