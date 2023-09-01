#ws to send hai for all text field

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
unames = driver.find_elements("xpath", "//input[@type='text']")
print(unames)
#<selenium.webdriver.remote.webelement.WebElement (session="b0f2b6af4b808e07f733262bc9854658", element="8B61A19EF226DA6145BB59AA8851B9A8_element_2")>, ... ]