XLS_URL=http://www.gamblingcommission.gov.uk/docs/Premises-licence-database-extract.xls
XLS=cache/premises.xls

addresses.tsv: $(XLS) addresses.py
	./addresses.py $(XLS) > $@

$(XLS):
	@mkdir -p cache
	curl -L -s $(XLS_URL) > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf

init:
	pip install -r requirements.txt
