#ws to click on forgot password link iwthout using click() method

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.facebook.com/")
sleep(2)
link = driver.find_element("xpath", "//a[.='Forgotten password?']")
link.send_keys(Keys.ENTER)