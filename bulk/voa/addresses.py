#!/usr/bin/env python3

import sys
import csv
import re
import io

output_fields = [ "test", "text" ]
sep = "\t"

if __name__ == '__main__':

    print(sep.join(output_fields))

    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='cp1252')

    # read map
    for row in csv.DictReader(input_stream, delimiter=" ", quotechar='"'):
        item = {}
        item['test'] = "voa:" + row['uarn']
        item['text'] = row['propaddr'] + ", " + row['postcde']

        print(sep.join([item[field] for field in output_fields]))
