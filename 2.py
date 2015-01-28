"""
Opens a webpage and goes to the link
Checks the title of the page to be specific
prints success to the comand prompt
closes the browsers
"""


from selenium import webdriver
# clicking on Welcome link.
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
driver.find_element_by_link_text("Welcome").click()
assert "Welcome" in driver.title
driver.close()