"""handle simple and confirmation alert in alert in below application
https://demoqa.com/alerts"""

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
sleep(5)
driver.find_element("xpath", "//button[@id='alertButton']").click()
alt = driver.switch_to.alert
sleep(3)
alt.accept()
sleep(5)
driver.find_element("xpath", "//button[@id='confirmButton']").click()
alt = driver.switch_to.alert
sleep(3)
alt.dismiss()
sleep(5)
driver.close()