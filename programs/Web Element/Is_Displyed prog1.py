#ws to verify login button is present or not

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.ksrtc.in/oprs-web/login/perform.do")
driver.maximize_window()
login = driver.find_element("xpath", "//input[@value='Login']")
print(login.is_displayed())       #True
log = driver.find_element("xpath", "//input[@value='Logi']")
print(log.is_displayed())           #NoSuchElementException