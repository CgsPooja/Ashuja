from selenium.webdriver import Chrome
import time

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.bing.com")
#driver.maximize_window()
#driver.fullscreen_window()
loc = driver.get_window_size()
print(loc)
print(loc['height'])
print(f" Width = {loc['width']}")
time.sleep(2)
driver.close()