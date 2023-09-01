#launch youtube --> search for a song --> play a song by ussing css selector locator

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
sleep(2)
driver.find_element("css selector","input[id ='search']").send_keys("Shivaji Maharaj Songs")
sleep(2)
driver.find_element("css selector","button[id = 'search-icon-legacy']").click()
sleep(5)
driver.find_element("css selector", "a[id='video-title']").click()

