#ws to perform right click on men tab in meesho

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.meesho.com/")
driver.maximize_window()
men = driver.find_element("xpath", "(//span[.='Men'])[1]")
a = ActionChains(driver)
a.context_click(men).perform()