#ws to print tag-name of a phone icon in byjus

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://byjus.com/")
driver.maximize_window()
call = driver.find_element("xpath", "//img[@class='call-icon']")
print(call.tag_name)            #img
