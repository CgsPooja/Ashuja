from selenium.webdriver import Chrome
from time import sleep

driver=Chrome(executable_path="../../drivers/chromedriver.exe")
driver.set_window_size(500,100)
sleep(2)
driver.close()