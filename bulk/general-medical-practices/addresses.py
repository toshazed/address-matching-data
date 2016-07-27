#!/usr/bin/env python3

import sys
import csv
import re

# "ORGANISATION CODE","NAME","NATIONAL GROUPING","HIGHER HEALTH AUTHORITY","ADDRESS LINE 1","ADDRESS LINE 2","ADDRESS LINE 3","ADDRESS LINE 4","ADDRESS LINE 5","POSTCODE","OPEN DATE","CLOSE DATE","STATUS","ORGANISATION SUB-TYPE CODE","COMMISSIONER","JOIN PARENT DATE","LEFT PARENT DATE","CONTACT TELEPHONE NUMBER","COL19","COL20","COL21","AMENDED RECORD INDICATOR","COL23","PROVIDER/PURCHASER","COL25","PRESCRIBING SETTING","COL27"

address_fields = ["ADDRESS LINE 1", "ADDRESS LINE 2", "ADDRESS LINE 3", "ADDRESS LINE 4", "ADDRESS LINE 5"]
fields = [ "test", "name", "text", "postcode" ]
sep = "\t"

if __name__ == '__main__':

    print(sep.join(fields))

    # read map
    for row in csv.DictReader(sys.stdin):
        item = {}
        item['test'] = "GMP:" + row['ORGANISATION CODE']
        item['name'] = row['NAME']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = re.sub(",+", ", ", item['text'])
        item['text'] = item['text'].strip(", ")

        item['postcode'] = row['POSTCODE']

        print(sep.join([item[field] for field in fields]))
