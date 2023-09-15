#extracting specific row column cell value

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

#step1
wb = open_workbook("../../excel/sample.xls")
#step2
sh = wb.sheet_by_name("Sheet1")
#step3
row = sh.row(3)
#step4
col = row[0]
#step5
print(col.value)
#'automation'
