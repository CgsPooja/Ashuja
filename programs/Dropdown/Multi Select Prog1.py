#ws to select multiple option in MSDD by index method

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(0)
s.select_by_index(2)
s.select_by_index(4)