#ws to switch back from child to immediate parent

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Dell/PycharmProjects/Selenium_M1/programs/Handling%20Frames/demo.html")
driver.maximize_window()
driver.find_element("id", "a1").send_keys("parent frame")
sleep(2)
driver.switch_to.frame("v1")
driver.find_element("id", "a2").send_keys("child1 frame")
sleep(2)
driver.switch_to.frame("v2")
driver.find_element("id", "a3").send_keys("child2 frame")
sleep(2)
driver.switch_to.parent_frame()
driver.find_element("id", "a2").send_keys("back to immediate parent")