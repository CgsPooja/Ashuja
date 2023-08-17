from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Dell/Downloads/demo.html")
pwd = driver.find_element("id","a111")
pwd.send_keys("demo@123")