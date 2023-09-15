from selenium.webdriver import  Chrome
from time import sleep

#ws to click on account in redbus
driver = Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "//span[.='Account']").click()
sleep(2)
driver.find_element("xpath", "//span[.='Login/ Sign Up']").click()
sleep(2)
driver.close()