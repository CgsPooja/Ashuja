#ws to select multiple option in MSDD by visible_text method

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_visible_text("7-9PM")
s.select_by_visible_text("7-9AM")
