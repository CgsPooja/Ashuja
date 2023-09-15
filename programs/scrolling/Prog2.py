#ws to scroll down to why medplus mart in medplus.com

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.medplusmart.com/")
driver.maximize_window()
sleep(5)
ele = driver.find_element("xpath", "//h6[.='Why MedPlusMart']")
loc = ele.location
sleep(4)
driver.execute_script(f"window.scrollBy({loc['x']}, {loc['y']})")
driver.close()