#wsto verify checkbox selected or not

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ch1 = driver.find_element("id", "a3")
ch2 = driver.find_element("id", "a4")
print(ch1.is_selected())                #False
print(ch2.is_selected())                #True