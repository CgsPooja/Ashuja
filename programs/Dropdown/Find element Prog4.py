#ws to print text in echo section

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element("xpath", "(//span[.='All'])[2]").click()
sleep(2)
driver.find_element("xpath", "//div[.='Echo & Alexa']").click()
sleep(2)
ops = driver.find_elements("xpath", "//div[.='echo & alexa']/../following-sibling::li/a")
for op in ops[:8]:
    print(op.text)

"""
All-new Echo Dot (4th Gen)
Echo Dot (3rd Gen)
Echo Show 8
All-new Echo (4th Gen)
Echo Show 5
Echo Studio
All-new Echo Show 10
See all devices with Alexa
"""