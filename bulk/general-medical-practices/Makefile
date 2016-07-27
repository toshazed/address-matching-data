CSV_URL=http://systems.hscic.gov.uk/data/ods/datadownloads/csv/epraccur.csv

addresses.tsv: cache/general-medical-practices.csv addresses.py
	./addresses.py < cache/general-medical-practices.csv > $@.new
	mv $@.new $@

cache/general-medical-practices.csv:
	@mkdir -p cache
	curl -L -s $(CSV_URL) | iconv -f ISO-8859-1 -t UTF-8 > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
