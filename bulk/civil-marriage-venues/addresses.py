#!/usr/bin/env python3

import sys
import csv
import re

# Address,,,,Postcode,Telephone number,
fields = [ "test", "text", "postcode" ]
address_fields = [ 0, 1, 2, 3 ]
sep = "\t"


if __name__ == '__main__':

    print(sep.join(fields))

    n = 0
    for row in csv.reader(sys.stdin):

        if n:
            item = {}
            item['test'] = 'civil-marriage-venue:' + str(n)
            item['text'] = ",".join([row[field] for field in address_fields])
            item['text'] = re.sub(",+", ", ", item['text'])
            item['text'] = item['text'].strip(" ,")

            item['postcode'] = row[4]

            print(sep.join([item[field] for field in fields]))

        n = n + 1
