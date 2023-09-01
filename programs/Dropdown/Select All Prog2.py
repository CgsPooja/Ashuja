#ws to select all the options from a DD

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
ops = s.options
for op in ops:
    print(op.text)

"""
Manual
SQL
Selenium
Python
Api
"""