#ws to check username is enabled or not

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
un1 = driver.find_element("id", "a1")           #True
un2 = driver.find_element("id", "a2")           #False
print(un1.is_enabled())
print(un2.is_enabled())