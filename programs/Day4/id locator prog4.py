from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
sleep(3)
driver.get("https://www.fb.com")
un = driver.find_element("id","email")
sleep(3)
un.send_keys("demouser")
pwd = driver.find_element("id","pass")
sleep(3)
pwd.send_keys("demo@123")
sleep(2)
driver.close()