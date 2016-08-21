URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/527996/approved_premises.csv
CSV=cache/premises.csv

addresses.tsv: addresses.py $(CSV)
	./addresses.py < $(CSV) > $@

$(CSV):
	@mkdir -p cache
	curl -L -s $(URL) > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
