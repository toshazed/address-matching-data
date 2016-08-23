#!/usr/bin/env python3

import sys
import xlrd
import csv
import re



['Account_Number', 'Account_Name', 'Trading_Names', 'Applicant_Property_name', 'Applicant_Address21', 'Applicant_City', 'Applicant_Postcode', 'Premises_Address1', 'Premises_Address2', 'Premises_City', 'Premises_Postcode', 'StatusDate', 'Activity', 'Local_Authority_Name', 'LicenceStatus']

address_fields = ['Premises_Address2', 'Premises_City']
fields = [ "test", "name", "text", "postcode" ]
sep = "\t"

if __name__ == '__main__':

    filename = sys.argv[1]

    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)

    headers = dict( (i, sheet.cell_value(0, i) ) for i in range(sheet.ncols) )

    print(sep.join(fields))

    for n in range(1, sheet.nrows):
        row = dict((headers[i], sheet.cell_value(n, i)) for i in range(sheet.ncols))

        item = {}
        item['test'] = "gambling:" + str(int(row['Account_Number']))
        item['name'] = row['Premises_Address1']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = re.sub(",+", ", ", item['text'])
        item['text'] = item['text'].strip(", ")

        item['postcode'] = row['Premises_Postcode']

        print(sep.join([item[field] for field in fields]))
