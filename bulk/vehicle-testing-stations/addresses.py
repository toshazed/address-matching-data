#!/usr/bin/env python3

import sys
import csv
import re

address_fields = ["VTS Trading Name", "VTS Address Line 1", "VTS Address Line 2", "VTS Address Line 3", "VTS Address Line 4"]
fields = [ "test", "text", "postcode" ]
sep = "\t"


if __name__ == '__main__':

    print(sep.join(fields))

    for row in csv.DictReader(sys.stdin):

        item = {}
        item['test'] = row['VTS Site Number']

        item['text'] = ",".join([row[field] for field in address_fields])
        item['text'] = re.sub(",+", ", ", item['text'])

        item['postcode'] = row['VTS Post Code']

        print(sep.join([item[field] for field in fields]))
