#ws to test actitime login page with multiple set of input

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
d = { sh.row_values(i)[0]:sh.row_values(i)[1] for i in range(1, sh.nrows) }
#{'demo': 'demo@123', 'sample': 'sample@1234', 'automation': 'automation123', 'admin': 'manager', 3543.0: '%$GFY^%$'}

for un, pwd in d.items():
    driver = Chrome()
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    driver.find_element("id", "username").send_keys(un)
    driver.find_element("name", "pwd").send_keys(pwd)
    driver.find_element("xpath", "//div[.='Login ']").click()
    driver.close()