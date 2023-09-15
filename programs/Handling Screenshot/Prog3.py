#example on saving screenshot with date-time as file name

from selenium.webdriver import Chrome
from time import sleep
from datetime import datetime

date = datetime.now()
d = date.strftime("%d-%m-%y %H-%M-%S")
driver = Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.save_screenshot(f"../../screen_shot/{d}.png")
sleep(2)
driver.close()