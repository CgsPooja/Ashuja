#ws to copy and paste user to password field

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = Chrome()
driver.get("https://www.facebook.com/")
sleep(2)
un = driver.find_element("id", "email")
un.send_keys("automationuser")
un.send_keys(Keys.CONTROL+"a")
un.send_keys(Keys.CONTROL+"c")
pw = driver.find_element("id", "pass")
pw.send_keys(Keys.CONTROL+"v")
btn = driver.find_element("name", "login")
btn.send_keys(Keys.ENTER)