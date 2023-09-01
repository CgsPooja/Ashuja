#ws to select and deselect option in MSDD

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(2)
s.select_by_value("v11")
s.select_by_visible_text("7-9PM")
sleep(2)
s.deselect_by_index(0)
s.deselect_by_value("v33")
s.deselect_by_visible_text("7-9PM")