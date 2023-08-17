from selenium.webdriver import Chrome
import time

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.google.com")
#driver.maximize_window()
driver.fullscreen_window()
pos = driver.get_window_position()
print(pos)
print(pos['x'])
print(pos['y'])
time.sleep(2)
driver.close()