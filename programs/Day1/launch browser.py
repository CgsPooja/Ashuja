from selenium.webdriver import Chrome

#write script to lounch empty chrome browser
#lounching empty chrome browser wit absolute path
c = Chrome(r"/drivers/chromedriver.exe")

#lounching empty chrome browser with relative path
c = Chrome("../../drivers/chromedriver.exe")

#Edge Browser
from selenium.webdriver import Edge

#write script to launch empty Edge browser
#lounching empty Edge browser with absolute path
e = Edge(r"/drivers/msedgedriver.exe")

#lounching empty edge browser with relative path
e = Edge("../../drivers/msedgedriver.exe")

#Firefox Browser
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

#write script to launch empty firefox browser
#lounching empty firefox browser with absolute path

#f = Firefox(r"C:\Users\Dell\PycharmProjects\Selenium_M1\drivers\geckodriver.exe")

option = Options()
option.binary_location= r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
f = Firefox(executable_path="../../drivers/geckodriver.exe", options=option)
