#!/usr/bin/env python3

import sys
import csv

fields = [ "test", "text" ]
sep = "\t"

if __name__ == '__main__':

    print(sep.join(fields))

    # read map
    for row in csv.DictReader(sys.stdin, delimiter=sep):
        row['test'] = row['name']

        row['text'] = "\\n".join(row['text'].strip().split("\n"))

        print(sep.join([row[field] for field in fields]))
