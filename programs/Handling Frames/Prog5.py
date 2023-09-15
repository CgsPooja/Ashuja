#example on "nosuchframe exception"

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
driver.maximize_window()
driver.find_element("id", "a1").send_keys("parent frame")
sleep(2)
driver.switch_to.frame("v3")
driver.find_element("id", "a2").send_keys("child1 frame")
#NoSuchFrameException: Message: v3