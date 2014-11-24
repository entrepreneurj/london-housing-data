#!/bin/bash

file=pp-complete.csv
london_file=pp-london.csv

# Compress Land Registry data to tar.gz to save downloads
#$(file).tar.gz: pp-london.csv
#	tar -zcvf $(file).tar.gz $(file)

# Filter London Postcodes
# http://www.doogal.co.uk/london_postcodes.php
# Remove time (midnight) from date
# Remove UUID
#$(info ***** Removing times from purchase dates) 
#$(info ***** Removes UUID from each record) 
pp-london.csv:$(file)
	$(info ***** Filtering houses containing London Postcodes)
	awk ' /"(EC|WC|E|N|NW|SE|SW|W|BR|CR|DA|EN|HA|IG|KT|RM|SM|TW|UB|WD){1}[1-9]{1,2}/ {print $$0}' $(file) >  pp-london.csv; \
	sed -i 's/ 00:00//g' $(london_file); \
	sed -i  's/\"{[A-Z0-9-]*}\",//g' $(london_file)



# Get data
$(file):
	$(info ***** Downloads complete price-paid-data from Land Registry)
	wget http://publicdata.landregistry.gov.uk/market-trend-data/price-paid-data/b/$(file)

# Delete old files
clean:
	rm pp-*

