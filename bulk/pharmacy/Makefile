CSV_URL=http://data.gov.uk/data/resource/nhschoices/Pharmacy.csv

addresses.tsv: cache/pharmacy.csv addresses.py
	./addresses.py < cache/pharmacy.csv > $@.new
	mv $@.new $@

cache/pharmacy.csv:
	@mkdir -p cache
	curl -L -s $(CSV_URL) | iconv -f ISO-8859-1 -t UTF-8 > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
