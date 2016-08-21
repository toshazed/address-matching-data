#!/usr/bin/env python3

import sys
import csv
import re

# "GeographicRegion","LicenceNumber","LicenceType","OperatorName","OperatorType","CorrespondenceAddress","OCAddress","TransportManager","NumberOfVehiclesAuthorised","NumberOfTrailersAuthorised","VehiclesSpecified","TrailersSpecified","DirectorOrPartner"

fields = [ "test", "name", "text" ]
sep = "\t"
addresses = {}

if __name__ == '__main__':

    print(sep.join(fields))

    for row in csv.DictReader(sys.stdin):

        if ('LicenceNumber' in row) and row['LicenceNumber'] and (row['LicenceNumber'] != 'LicenceNumber'):
            item = {}
            item['name'] = row['OperatorName'].strip()

            n = 0
            for text in row['CorrespondenceAddress'].split(";") + row['OCAddress'].split(";"):

                # unsure if to remove " GB " found in many addresses ..
                text = " ".join(text.split())

                if text and text not in addresses:
                    n = n + 1
                    item['test'] = row['LicenceNumber'].strip() + "_" + str(n)
                    item['text'] = text
                    print(sep.join([item[field] for field in fields]))

                    addresses[text] = 1

