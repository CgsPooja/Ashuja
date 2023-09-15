#ws to click on "cancel" in alert and confirmation popup

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "(//a[contains(.,'Login')])[2]").click()
sleep(2)
alt = driver.switch_to.alert
#alt.dismiss()
alt.accept()