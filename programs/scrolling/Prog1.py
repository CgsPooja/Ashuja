#ws to scroll down in bigbasket

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
sleep(8)
driver.execute_script("window.scrollBy(0, 700)")
driver.close()