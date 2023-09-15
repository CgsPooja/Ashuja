#extracting specific row

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

#step1
wb = open_workbook("../../excel/sample.xls")
#step2
sh = wb.sheet_by_name("Sheet1")
#step3
row = sh.row(3)
print(row)
#[text:'automation', text:'automation123']
#        0                    1