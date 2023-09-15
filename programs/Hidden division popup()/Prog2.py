from selenium.webdriver import  Chrome
from time import sleep

#ws to select date of departure
driver = Chrome()
driver.get("https://www.ksrtc.in/oprs-web/")
driver.maximize_window()
sleep(4)
driver.find_element("xpath", "//input[@value='Date Of Departure']").click()
sleep(4)
driver.find_element("xpath", "//a[.='5']").click()
sleep(2)
driver.close()
