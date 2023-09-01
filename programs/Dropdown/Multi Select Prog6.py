#ws to select "Oct" option in facebook month dropdown

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://www.facebook.com/")
driver.find_element("xpath", "//a[.='Create new account']").click()
sleep(2)
month = driver.find_element("xpath", "//select[@title='Month']")
s = Select(month)
s.select_by_value("10")