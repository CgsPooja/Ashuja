#ws to handle simple alert in demowebshop

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//input[@value='Search']").click()
alert = driver.switch_to.alert
sleep(2)
alert.accept()
    #(or)
#alert.dismiss()
#NoAlertPresentException: Message: no such alert