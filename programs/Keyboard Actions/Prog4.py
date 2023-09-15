#by using actions chain class handling keyboard cations

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
a = ActionChains(driver)
a.key_down(Keys.CONTROL).perform()
a.send_keys("A").perform()
a.key_up(Keys.CONTROL).perform()
a.send_keys("A").perform()