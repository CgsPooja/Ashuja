from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Dell/Downloads/demo%20table.html")
driver.maximize_window()
driver.find_element("xpath","//td[.='Toby']/../td[3]").click()
sleep(10)
driver.close()
