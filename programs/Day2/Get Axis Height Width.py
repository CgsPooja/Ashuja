from selenium.webdriver import Chrome
import time

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https:www.bing.com")
#driver.maximize_window()
#driver.fullscreen_window()
Rect = driver.get_window_rect()
print(Rect)
print(f"Height = {Rect['height']}")
print(f"Width = {Rect['width']}")
print(f"X Axis = {Rect['x']}")
print(f"Y Axis = {Rect['y']}")
time.sleep(3)
driver.close()