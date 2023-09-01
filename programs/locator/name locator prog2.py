#ws to enter username in facebook

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)
driver.find_element("name","email").send_keys("malipoja2@mail.com")
sleep(2)
driver.close()