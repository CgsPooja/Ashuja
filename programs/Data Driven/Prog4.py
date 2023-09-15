#ws to print total number of rows and coulmns present in excel file

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
print(row_count)        #6
col_count = sh.ncols
print(col_count)        #2
