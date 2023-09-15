#ws to scroll down to why medplus mart and scroll up to topoffers in medplsu.com

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://www.medplusmart.com/")
driver.maximize_window()
sleep(3)
ele = driver.find_element("xpath", "//h6[.='Why MedPlusMart']")
loc = ele.location
driver.execute_script(f"window.scrollBy({loc['x']}, {loc['y']})")
sleep(3)
ele1 = driver.find_element("xpath", "//h5[.='Top Offers']")
lo = ele1.location
driver.execute_script(f"window.scrollTo({lo['x']}, {lo['y']})")
driver.close()