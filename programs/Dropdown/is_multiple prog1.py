#ws to verify a DD is multi select or not

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ssdd = driver.find_element("id", "a1")
msdd = driver.find_element("id", "a2")
s1 = Select(ssdd)           #single selectDD
print(s1.is_multiple)   #None
s2 = Select(msdd)           #multi selectDD
print(s2.is_multiple)   #True