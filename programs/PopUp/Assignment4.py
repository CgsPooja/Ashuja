"""(click on last "click me" button --> enter ur name and click on "ok")
https://demo.guru99.com/test/delete_customer.php"""

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "//input[@name='cusid']").send_keys("111")
sleep(2)
driver.find_element("xpath", "//input[@type='submit']").click()
alt = driver.switch_to.alert
sleep(2)
alt.accept()
sleep(2)
alt = driver.switch_to.alert
sleep(2)
alt.accept()
sleep(2)
driver.close()
