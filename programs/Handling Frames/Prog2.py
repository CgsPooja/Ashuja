#ws to switch to frame by index as argument

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
driver.maximize_window()
driver.find_element("id", "a1").send_keys("parent frame")
sleep(2)
driver.switch_to.frame(0)
driver.find_element("id", "a2").send_keys("child1 frame")
sleep(2)
driver.switch_to.frame(0)
driver.find_element("id", "a3").send_keys("child2 frame")