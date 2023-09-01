#ws to verify checkbox is selected or not in zomato

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.zomato.com/bangalore")
driver.find_element("xpath", "//a[.='Sign up']").click()
ch = driver.find_element("xpath", "//input[@type='checkbox']")
print(ch.is_selected())             #False
ch.click()
print(ch.is_selected())             #True