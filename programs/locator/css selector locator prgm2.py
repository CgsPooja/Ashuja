#ws to automate on dunzo

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.https://www.dunzo.com/pune")
driver.maximize_window()
sleep(2)
driver.find_element("css selector", "button[data-tip='header-business-options']").click()
sleep(5)
driver.find_element("css selector","div[class ='sc-AxjAm StDqM sc-jbkzle-3 ciacIP']").click()
sleep(2)
driver.find_element("css selector","input[id = 'firstname-input']").send_keys("Baburao")
sleep(2)
driver.find_element("css selector","input[name ='company']").send_keys("chavan industries")
sleep(2)
driver.find_element("css selector","select[name ='hs-form__field__input is-placeholder']").click()
driver.find_element("css selector", "option [label = 'Chennai']").click()
sleep(2)
driver.find_element("css selector","input[type='email']").send_keys("test@mail.com")
sleep(2)
driver.find_element("css selector","input[id='phone-input']").send_keys("7458787457")
sleep(2)
driver.find_element("css selector","input[class='hs-form__field__input']").send_keys("www.facebook.com")
sleep(2)
driver.find_element("css selector","button[type='submit']").click()
sleep(2)
driver.quit()