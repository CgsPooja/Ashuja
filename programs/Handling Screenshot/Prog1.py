#example on saving screenshot in current location

from selenium.webdriver import Chrome
from time import sleep
from datetime import datetime

driver = Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.save_screenshot("../../screen_shot/defect1.png")
sleep(2)
driver.close()