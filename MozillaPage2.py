from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='site-header']/mkt-header-nav/li[2]/a").click()
assert "Popular | Firefox Marketplace" in driver.title

driver.find_element_by_xpath("//*[@id='ph_1']/ul/li[25]/button").click()

driver.find_element_by_xpath("//*[@id='newsletter-footer']/div/form/input").send_keys('bishnucit1@gmail.com')
driver.find_elements_by_xpath("//*[@id='newsletter-footer']/div/form/button[1]").click()
assert "privacy" in driver.page_source
driver.find_element_by_xpath("//*[@id='id_newsletter_privacy']").click()
driver.find_elements_by_xpath("//*[@id='newsletter-footer']/div/form/button[1]").click()
driver.implicitly_wait(5)

assert "success" in driver.page_source



driver.close()
