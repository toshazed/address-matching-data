DATE_NUMERIC:=$(shell date +"%Y%m")
DATE_TEXT:=$(shell date +"%B")
CHARITY_COMMISSION_URL=http://apps.charitycommission.gov.uk/data/$(DATE_NUMERIC)/extract1/RegPlusExtract_$(DATE_TEXT)_2016.zip

addresses.tsv: addresses.py cache/extract_charity.bcp
	./addresses.py < cache/extract_charity.bcp > $@.new
	mv $@.new $@

# download from EDUBASE
# - contains invalid UTF-8 characters ..
cache/RegPlusExtract.zip:
	@mkdir -p cache
	curl -s $(CHARITY_COMMISSION_URL) > $@.new
	mv $@.new $@

cache/extract_charity.bcp: cache/RegPlusExtract.zip
	unzip -p cache/RegPlusExtract.zip extract_charity.bcp > $@.new
	mv $@.new $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	rm -f cache/*.new
