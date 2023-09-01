#ws to clear/remove default value present in text field

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
un = driver.find_element("id", "a1")
un.clear()
un.send_keys("automation user")
sleep(5)
driver.close()