#ws to validate register now button isdisabled or not

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
register = driver.find_element("xpath", "//button[.='Register now']")
if register.is_enabled():
    print("register now button is-enabled")
else:
    print("register now button is-disabled")