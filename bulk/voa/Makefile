DATE:=$(shell date +"%Y%m%d")
EDUBASE_URL=http://www.education.gov.uk/edubase/edubasealldata$(DATE).csv

addresses.tsv: addresses.py VOA-2010-2015-09.txt
	./addresses.py < VOA-2010-2015-09.txt > $@.new
	mv $@.new $@

VOA-2010-2015-09.txt:
	@echo "Please get file $@ and put it in this directory. Remember not to commit it, as it contains restricted data."

prune::
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	rm -f addresses.tsv.new
