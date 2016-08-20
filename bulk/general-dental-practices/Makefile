CSV_URL=http://systems.hscic.gov.uk/data/ods/datadownloads/csv/egdpprac.csv

addresses.tsv: cache/practices.csv addresses.py
	./addresses.py < cache/practices.csv > $@

cache/practices.csv:
	@mkdir -p cache
	curl -L -s $(CSV_URL) > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
