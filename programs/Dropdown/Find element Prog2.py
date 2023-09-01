#ws to send hai for all text field

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
unames = driver.find_elements("xpath", "//input[@type='text']")
for un in unames:
    un.send_keys("hai")