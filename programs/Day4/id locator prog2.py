from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Dell/Downloads/demo.html")

username = driver.find_element("id","a1")
username.send_keys("demouser")


pwd = driver.find_element("id", "a1")
pwd.send_keys("demo@123")