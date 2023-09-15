#ws to enter mobile number in redbus login page

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//span[.='Account']").click()
sleep(3)
driver.find_element("xpath", "//span[.='Login/ Sign Up']").click()
sleep(3)
frame = driver.find_element("xpath", "//iframe[@class='modalIframe']")
sleep(3)
driver.switch_to.frame(frame)
sleep(4)
driver.find_element("xpath", "//input[@type='number']").send_keys("566565454")