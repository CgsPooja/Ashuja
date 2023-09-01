#ws to select an option in SSDD by value method

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
s.select_by_value("v5")