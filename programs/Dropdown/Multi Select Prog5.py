#ws to select and deselect option in SSDD

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
s.select_by_index(2)
s.deselect_by_index(2)
#NotImplementedError: You may only deselect options of a multi-select