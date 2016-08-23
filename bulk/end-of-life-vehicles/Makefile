XLS_URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/542559/LIT_7762.xls
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
