#!/usr/bin/env python3

import sys
import collections
import re
import io

#address_fields = ["EstablishmentName", "Street", "Locality", "Address3", "Town", "County (name)", "Postcode"]
field_names = [ 'regno', 'subno', 'name', 'orgtype', 'gd', 'aob', 'aob_defined', 'nhs', 'ha_no', 'corr', 'add1', 'add2', 'add3', 'add4', 'add5', 'postcode', 'phone', 'fax' ]
address_fields = [ 'add1', 'add2', 'add3', 'add4', 'add5' ]
output_fields = [ "test", "name", "text", "postcode" ]
sep = "\t"


# BCP is a Microsoft SQL Server export format.
#    @**@ separates fields
#    *@@* separates rows
# There is no escaping, it is assumed those values don't appear in field contents.
def parse_bcp(content):
    l = []
    splits = re.split("(\@\*\*\@|\*\@\@\*)", content)
    for item in splits:
        if item == '*@@*':
            yield l
            l = []
            continue
        if item == '@**@':
            continue

        item = item or ""
        item = item.strip()
        l.append(item)

if __name__ == '__main__':

    print(sep.join(output_fields))

    # read map
    binary_content = sys.stdin.buffer.read()
    # most of the input is in cp1252 except one word CAFE with a UTF-8 e-acute
    # (0x90), we replace it for the cp1252 version (0xc9).
    binary_content = binary_content.replace(b'CAF\x90', b'CAF\xc9')
    content = binary_content.decode('cp1252')

    for fields in parse_bcp(content):
        items = collections.OrderedDict(zip(field_names, fields))

        output = {}
        output['test'] = "charity:" + items['regno']

        output['name'] = items['name']

        output['text'] = ",".join([items[field] for field in address_fields if items[field] != ""])
        output['text'] = re.sub(",+", ", ", output['text'])
        if output['text'] == "":
            continue

        output['postcode'] = items['postcode']

        print(sep.join([output[field] for field in output_fields]))

