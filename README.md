# Address matching data

Test cases and other data for training and testing address matching algorithms.

# Test case format

Test cases are held in tab-separated format files with the following columns:

- test — an identifier for the test case which should be unique across all tests
- name — the addressee or name of the business (if separable)
- text — address text to be matched, newlines should be encoded as '\n'
- postcode — an optional, separate postcode (if separable)
- uprns — one or more UPRN values in decimal which could match the address, separated by semicolon ';'
- notes — an explanation of the test

A test case may contain additional fields for information.

# Bulk datasets

The [bulk](bulk) directory contains addresses found in bulk in open data, to be matched.

Few bulk datasets currently contain resolved UPRNs, but can form the basis of test cases as we build registers.

# Licence

The software in this project is open source, covered by [LICENSE](LICENSE) file.

The data held in this repository is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

Data downloaded by the build process may be covered by different copyright and terms.
