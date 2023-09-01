#ws to mouse hover on fashions in flipkart

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element("xpath", "//button[.='✕']").click()
fashion = driver.find_element("xpath", "(//div[.='Fashion'])[3]")
a = ActionChains(driver)
a.move_to_element(fashion).perform()