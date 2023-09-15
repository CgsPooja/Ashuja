"""select a user defined date in ksrtc
https://www.ksrtc.in/oprs-web/"""

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.find_element("xpath", "//input[@value='Date Of Departure']").click()
sleep(4)
driver.find_element("xpath", "//a[.='5']").click()
sleep(2)
driver.close()