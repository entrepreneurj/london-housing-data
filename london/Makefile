#!/bin/bash

#
# Makefile for Brockley Housing Prices Analyis
# Author: Joe Letts
# Date 23/11/2014
#

DIR := ${CURDIR}
data_file=$(DIR)/../pp-london.csv
code_point_data=../vendor/Ordnance_Survey/code_point/Data/CSV
post_code_stem=ec wc e n nw se sw w

london.jpg: london_price_date_location.csv post_code_locations.csv
	$(info *****Creating images via script)
	python data_export.py

# CSV of London house prices, purchase dates and postcodes ($2,$3,$4)
london_price_date_location.csv: london_locations.csv post_code_locations.csv
	$(info *****Creating CSV of house prices, dates and locations in Greater London)
	awk 'BEGIN {FS = "\",?\"?";} {print "\"" $$2 "\",\"" $$3 "\",\"" $$4 "\"";}' london_locations.csv > london_price_date_location.csv

# Homes in London
london_locations.csv: $(data_file)
	$(info *****Filtering data to find locations in Greater London (excluding surrounding areas, e.g. Croydon, Romford))
	awk 'BEGIN {FS = "\",?\"?";} $$4 ~ /^(EC|WC|E|N|NW|SE|SW|W)/ {print $$0;}' $(data_file) > london_locations.csv

# CSV of SE4 postcodes, eastings and northings
london_pc_locations.csv: $(code_point_data)/*.csv
	$(info *****Merging postcode location data for all postcodes in London)
	for f in $(post_code_stem); do tail -n +2 $(code_point_data)/$$f.csv >> london_pc_locations.csv; done 

post_code_locations.csv: london_pc_locations.csv
	$(info *****Creating CSV of London postcodes and associated Eastings and Northings)
	awk 'BEGIN { FS="\"?,?\"?"; } {print "\"" $$2 "\",\"" $$4 "\",\"" $$5 "\"";}' london_pc_locations.csv > post_code_locations.csv

clean:
	rm ./*.csv ./*.svg ./*.png ./*.jpg
