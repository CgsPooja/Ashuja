#ws to perform drag and drop in sample webpage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
src = driver.find_element("xpath", "//div[@id='draggable']")
dest = driver.find_element("xpath", "//div[@id='droppable']")
a = ActionChains(driver)
sleep(2)
a.drag_and_drop(src, dest).perform()