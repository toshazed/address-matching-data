#!/usr/bin/env python3

import sys
import csv
import re

# "{816D2B17-C653-4CCC-8B8A-3EDD66EB464F}","69000","1995-04-03 00:00","PO14 2QN","S","N","F","34","","HAROLD ROAD","FAREHAM","FAREHAM","FAREHAM","HAMPSHIRE","A","A"

address_cols = range(7, 13)
fields = [ "text", "postcode" ]
sep = "\t"


if __name__ == '__main__':

    print(sep.join(fields))

    # read map
    for row in csv.reader(sys.stdin):

        item = {}
        item['text'] = ",".join([row[col] for col in address_cols if row[col-1] != row[col]])
        item['text'] = re.sub(",+", ", ", item['text'])

        item['postcode'] = row[3]

        print(sep.join([item[field] for field in fields]))
