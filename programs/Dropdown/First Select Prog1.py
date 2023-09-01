#example on first selected option property

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
msdd = driver.find_element("id", "a2")
s = Select(msdd)
s.select_by_index(2)        #12pm
s.select_by_index(0)        #7am
s.select_by_index(4)        #4pm
print(s.first_selected_option.text)     #7am