import xlrd
from xlrd.xldate import XLDateAmbiguous

file = 'ch02-xlsxdata.xlsx'

wb = xlrd.open_workbook(filename=file)

ws = wb.sheet_by_name('Sheet1')

dataset = []

for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
        if ws.cell_type(r, c) == xlrd.XL_CELL_DATE:
            try:
                print ws.cell_type(r, c)
                from datetime import datetime
                date_value = xlrd.xldate_as_tuple(ws.cell(r, c).value, wb.datemode)
                print datetime(*date_value)
            except XLDateAmbiguous as e:
                print e
    dataset.append(col)

from pprint import pprint

pprint(dataset)


