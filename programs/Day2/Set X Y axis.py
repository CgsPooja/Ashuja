from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.ajio.com")
driver.set_window_position(0,0)
sleep(2)
driver.close()