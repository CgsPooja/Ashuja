#ws to click on "ok" in alert and confirmation popup

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "(//a[contains(.,'Login')])[2]").click()
alt = driver.switch_to.alert
alt.accept()