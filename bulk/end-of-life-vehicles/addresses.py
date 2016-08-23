#!/usr/bin/env python3

import sys
import xlrd
import csv
import re

fields = [ "test", "name", "text", "postcode" ]
sep = "\t"

if __name__ == '__main__':

    filename = sys.argv[1]

    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)

    headers = dict( (i, sheet.cell_value(4, i) ) for i in range(sheet.ncols) )

    print(sep.join(fields))

    for n in range(5, sheet.nrows):
        row = dict((headers[i], sheet.cell_value(n, i)) for i in range(sheet.ncols))

        item = {}
        item['test'] = "end-of-life-vehicle:" + row['EPR Permit Ref']
        item['name'] = row['Permit holder'].strip()

        item['text'] = row['Address']
        item['text'] = re.sub(",+", ", ", item['text'])

        item['postcode'] = row['Postcode']

        if item['name'] != '' and item['text'] != '':
            print(sep.join([item[field] for field in fields]))
