#ws to click on show more and click on onion in bigbasket

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
sleep(2)
driver.find_element("link text", "Show More").click()
sleep(2)
driver.find_element("link text", "Potato").click()
sleep(5)
driver.quit()