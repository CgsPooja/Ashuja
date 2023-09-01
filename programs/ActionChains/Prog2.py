#ws to mousehover on study material and click on Frank solutions for class 10

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://byjus.com/")
driver.maximize_window()
study = driver.find_element("xpath", "//a[.='Study Materials']")
a = ActionChains(driver)
a.move_to_element(study).perform()
icse = driver.find_element("xpath", "(//a[.='ICSE'])[1]")
a.move_to_element(icse).perform()
frank = driver.find_element("xpath", "//a[.='Frank Solutions']")
a.move_to_element(frank).perform()
driver.find_element("xpath", "//a[.='Frank Solutions for Class 10 Maths']").click()