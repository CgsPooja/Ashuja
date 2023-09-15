#ws to click on settings in twitter tab

from selenium.webdriver import  Chrome
from time import sleep


driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//a[.='Facebook']").click()
sleep(3)
driver.find_element("xpath", "//a[.='Google+']").click()
sleep(3)
driver.find_element("xpath", "//a[.='Twitter']").click()
sleep(2)
driver.find_element("xpath", "//a[@href='/settings']").click()
sleep(2)
driver.close()
