#ws to print height,width,x and y cordinate of an english link in wikipedia

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.wikipedia.org/")
sleep(3)
eng = driver.find_element("xpath", "//strong[.='English']")
s = eng.size
print(s)                #{'height': 24, 'width': 156}
l = eng.location
print(l)                #{'x': 298, 'y': 137}
r = eng.rect
print(r)                #{'height': 24, 'width': 156, 'x': 297.90625, 'y': 137.25}