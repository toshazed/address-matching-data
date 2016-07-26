DATE:=$(shell date +"%Y%m%d")
EDUBASE_URL=http://www.education.gov.uk/edubase/edubasealldata$(DATE).csv

addresses.tsv: addresses.py cache/edubase.csv
	./addresses.py < cache/edubase.csv > $@.new
	mv $@.new $@

# download from EDUBASE
# - contains invalid UTF-8 characters ..
cache/edubase.csv:
	@mkdir -p cache
	curl -s $(EDUBASE_URL) | iconv -f ISO-8859-1 -t UTF-8 > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
