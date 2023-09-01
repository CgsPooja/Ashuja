#ws to print all options in ascending order

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://www.facebook.com/")
driver.find_element("xpath", "//a[.='Create new account']").click()
sleep(2)
month = driver.find_element("xpath", "//select[@title='Month']")
s = Select(month)
ops = s.options
for op in ops:
    l.append(op.text)
l.sort()
print(l)        #['Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep']