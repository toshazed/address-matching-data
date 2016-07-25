# Address matching data

Test cases and other data for training and testing address matching algorithms.

# Test case format

Test cases are held in tab-separated format files with the following columns:

- [test](http://field.discovery.openregister.org/field/test) — an identifier for the test case which should be unique across all tests
- [name](http://field.discovery.openregister.org/field/name) — a name for the test
- [text](http://field.alpha.openregister.org/field/text) — the address encoded as lines of text, newlines are encoded as '\n'
- uprns — a list of UPRN values which could match the address, separated by ';'

A test case may contain additional fields for information.

# Building bulk datasets

    $ make

# Licence

The software in this project is open source, covered by [LICENSE](LICENSE) file.

The data held in this repository is [© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

Data downloaded by the build process may be covered by different copyright and terms.
