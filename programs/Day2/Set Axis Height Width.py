from selenium.webdriver import Chrome
from time import sleep

driver= Chrome(executable_path="../../drivers/chromedriver.exe")
driver.set_window_rect(87,55,273,800)
sleep(3)
driver.close()