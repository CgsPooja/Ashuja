#ws to backspace 4 times in username field

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.facebook.com/")
sleep(2)
un = driver.find_element("id", "email")
un.send_keys("automationuser")
for i in range(4):
    un.send_keys(Keys.BACKSPACE)
    sleep(1)