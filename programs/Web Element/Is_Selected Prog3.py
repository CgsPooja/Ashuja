#example on check box develope by other tag

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
ch = driver.find_element("xpath", "//a[contains(@class,'checkbox-wrap on')]")
print(ch.is_selected())         #False