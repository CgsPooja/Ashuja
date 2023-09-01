#ws to print text of a alert and click on ok

from selenium.webdriver import  Chrome
from time import sleep

driver = Chrome()
driver.get("https://epfoportals.epfindia.gov.in/iwu/")
driver.maximize_window()
driver.find_element("xpath", "//button[.='LogIn']").click()
alert = driver.switch_to.alert
print(alert.text)       #User name or password field can  not be empty!
alert.accept()