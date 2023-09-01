#ws to click on movie in bookmyshow

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://in.bookmyshow.com/explore/home/pune")
driver.maximize_window()
driver.find_element("tag name","a")
sleep(5)
driver.close()