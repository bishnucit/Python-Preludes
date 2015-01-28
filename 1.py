"""
Opens a webpage and goes to the link
Checks the title of the page to be specific
prints success to the comand prompt
closes the browsers
"""



from selenium import webdriver
#opening the webpage
driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
assert "Welcome" in driver.title
print ("success")
driver.close()