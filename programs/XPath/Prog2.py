#ws to click on login in zomato

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.zomato.com/bangalore")
driver.maximize_window()
driver.find_element("xpath","//a[.='Log in']").click()
sleep(2)
driver.close()
