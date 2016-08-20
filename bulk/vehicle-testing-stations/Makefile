# https://data.gov.uk/dataset/mot-active-vts
URL='http://www.vosa.gov.uk/vosa/images/motsitelist2015.csv'

addresses.tsv:	cache/motsites.csv addresses.py
	addresses.py < cache/motsites.csv > $@

cache/motsites.csv:
	mkdir -p cache
	curl -s -L $(URL) > $@

clean:
	rm -rf cache
