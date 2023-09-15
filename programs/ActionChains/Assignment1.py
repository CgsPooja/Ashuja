#mouse hover on study material-->mouse hover on CBSE--> mouse hover on physics --> print all options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://byjus.com/")
driver.maximize_window()
sleep(3)
study = driver.find_element("xpath", "//a[contains(.,'Study Materials')]")
a = ActionChains(driver)
a.move_to_element(study).perform()
sleep(2)
cbse = driver.find_element("xpath", "//a[contains(.,'CBSE')]")
a.move_to_element(cbse).perform()
sleep(2)
phy = driver.find_element("xpath", "//a[.='PHYSICS']")
a.move_to_element(phy).perform()
sleep(3)
ops = driver.find_elements("xpath", "(//ul[@class='more-less-open'])[1]/li/a")
for op in ops:
    print(op.text)
    driver.close()







