URL=http://www.vosa.gov.uk/vosa/apps/olbs/OLBSLicenceReport_

REGIONS=\
	East%20of%20England \
	North%20West%20of%20England \
	London%20and%20the%20South%20East%20of%20England \
	West%20Midlands \
	North%20East%20of%20England \
	Scotland \
	Wales \
	West%20of%20England

CSVS=$(REGIONS:%=cache/%.csv)

addresses.tsv: addresses.py $(CSVS)
	cat $(CSVS) | ./addresses.py > $@

cache/%.csv:
	@mkdir -p cache
	curl -L -s $(URL)$(@F) | iconv -f ISO-8859-1 -t UTF-8 > $@

prune::
	rm -rf cache
	rm -rf addresses.tsv

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
