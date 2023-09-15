

"""
stepno      action/description                      input                       expected result
======      ==================                      =====                       ===============
1           open browser and enter              http://localhost/login.do       login page should be
            url.                                                                 display.
2           enter valid UN and valid            UN:admin                        home page should be display.
            PWD and click on login button.      PWD:manager
3           click on logout button.                 NA                          login page should be display.
"""

from selenium.webdriver import Chrome
from time import sleep
from datetime import datetime

driver = Chrome()
def take_screenshot():
    d = datetime.now()
    dt = d.strftime("%d-%m-%y %H-%M-%S")
    driver.save_screenshot(f"../screen_shot/{dt}.png")

def verify_title(etitle):
 assert driver.title == etitle, take_screenshot()

driver.get("http://localhost/login.do")
driver.maximize_window()
verify_title("actiTIME - Login")
driver.find_element("id", "username").send_keys("admin")
driver.find_element("name", "pwd").send_keys("manager")
driver.find_element("xpath", "//div[.='Login ']").click()
verify_title("actiTIME - Enter Time-Track")
driver.find_element("xpath", "//a[.='Logout']").click()
verify_title("actiTIME - Login")
driver.close()