#ws to close parent tab

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.close()