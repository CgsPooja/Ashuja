#ws to extract print of earpodin apple.com

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.apple.com/in/shop/accessories/all/headphones-speakers?f=apple-overear-sport&fh=47d1%2B3214%2B45aa%2B45ab&page=1")
driver.maximize_window()
earpod = driver.find_element("xpath", "//a[@data-evar11='MQD83|category']")
print(earpod.text)                #AirPods Pro (2nd generation)