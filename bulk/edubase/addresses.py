#!/usr/bin/env python3

import sys
import csv
import re

address_fields = ["Street", "Locality", "Address3", "Town", "County (name)", "Postcode"]
fields = [ "test", "name", "text" ]
sep = "\t"

if __name__ == '__main__':

    print(sep.join(fields))

    # read map
    for row in csv.DictReader(sys.stdin):
        item = {}
        item['test'] = "school:" + row['URN']
        item['name'] = row['EstablishmentName']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = re.sub(",+", ", ", item['text'])

        print(sep.join([item[field] for field in fields]))
