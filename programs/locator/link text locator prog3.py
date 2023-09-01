#ws to click on dream11 in demrem11 fantasycricket

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.dream11.com/dream11-team-today")
driver.maximize_window()
sleep(2)
link = driver.find_element("link text", "About Us")
link.click()
sleep(5)
driver.quit()
