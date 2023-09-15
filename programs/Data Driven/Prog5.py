#wp to print all cell/column value of a specific row

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2)
print(data)
#['sample', 'sample@1234']
