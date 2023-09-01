#ws to click on hotels in makemytrip


from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.redbus.in/")
driver.maximize_window()
sleep(2)
driver. find_element("class name","name_rb_vertical").click()
sleep(4)
driver.close()
