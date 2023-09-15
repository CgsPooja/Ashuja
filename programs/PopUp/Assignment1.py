"""handle simple alert in alert in below application
https://www.ksrtc.in/oprs-web/login/show.do"""

from selenium.webdriver import  Chrome
from time import sleep
driver = Chrome()
driver.get("https://www.ksrtc.in/oprs-web/login/show.do")
driver.maximize_window()
driver.find_element("xpath", "//input[@id='submitBtn']").click()
sleep(2)
alt = driver.switch_to.alert
alt.accept()
sleep(3)
driver.close()

