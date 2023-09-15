#ws to click on login/create account --> click on google icon --> print title of child n parent tab -->
#click on create new account --> enter user name

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//div[@class='S9gUrf-YoZ4jf']").click()