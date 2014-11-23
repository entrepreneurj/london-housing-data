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
	python data_export.py
# CSV of SE4 House prices, purchase dates and postcodes ($2,$3,$4)
london_price_date_location.csv: london_locations.csv post_code_locations.csv
	awk 'BEGIN {FS = "\",?\"?";} {print "\"" $$2 "\",\"" $$3 "\",\"" $$4 "\"";}' london_locations.csv > london_price_date_location.csv

# Homes in Brockley
london_locations.csv: $(data_file)
	awk 'BEGIN {FS = "\",?\"?";} $$4 ~ /^(EC|WC|E|N|NW|SE|SW|W)/ {print $$0;}' $(data_file) > london_locations.csv

# CSV of SE4 postcodes, eastings and northings
london_pc_locations.csv: $(code_point_data)/*.csv
	for f in $(post_code_stem); do tail -n +2 $(code_point_data)/$$f.csv >> london_pc_locations.csv; done 

post_code_locations.csv: london_pc_locations.csv
	awk 'BEGIN { FS="\"?,?\"?"; } {print "\"" $$2 "\",\"" $$4 "\",\"" $$5 "\"";}' london_pc_locations.csv > post_code_locations.csv

clean:
	rm ./*.csv ./*.svg ./*.png ./*.jpg
