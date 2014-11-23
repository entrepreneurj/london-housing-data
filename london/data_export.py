

import csv
import svgwrite	as svg

import cairosvg as cairos
from PIL import Image
pcs = {'bounds': {'x': {'min':1000000000, 'max':0},'y': {'min':10000000000000, 'max':0} } }

with open('post_code_locations.csv','r') as location_file:
    
    loc_reader=csv.DictReader(location_file, fieldnames=['post_code', 'eastings', 'northings'], 
                    delimiter=',', quotechar='"') 
	
    for loc in loc_reader:
        x = int(loc['eastings'])
        y = int(loc['northings'])

        pcs[loc["post_code"]]= \
            { 'eastings': x, 'northings': y}

        # finds bounds for postcodes
        pcs['bounds']['x']['max'] = max(pcs['bounds']['x']['max'],x)
        pcs['bounds']['x']['min'] = min(pcs['bounds']['x']['min'],x)
        pcs['bounds']['y']['min'] = min(pcs['bounds']['y']['min'],y)
        pcs['bounds']['y']['max'] = max(pcs['bounds']['y']['max'],y)
print pcs['bounds']
d_width = (pcs['bounds']['x']['max'] - pcs['bounds']['x']['min'] + 1000)/2
d_height = (pcs['bounds']['y']['max'] - pcs['bounds']['y']['min'] + 1000)/2
print d_height/2, d_width/2
dwg = svg.Drawing(filename='london.svg',size=("%s" % d_height, "%s" % d_width ))

for pc, loc in pcs.iteritems():
    if pc is not "bounds":
        cx = int(loc['eastings']-pcs['bounds']['x']['min'])
        cy = int(loc['northings']-pcs['bounds']['y']['min'])
        dwg.add( dwg.circle( (cx/2,d_height -cy/2), r=10, opacity=0.8, fill="black") )
        #dwg.add( dwg.circle( (cx/2,cy/2), r=12, stroke="black", stroke_width=3, opacity=0.5, fill="red") )
dwg.saveas('london_postcodes.svg')
cairos.svg2png(file_obj=open('london_postcodes.svg','r'), write_to='london.png')
pngImage= Image.open('london.png')
jpgImage = Image.new("RGBA", pngImage.size, (255,255,255,255))
jpgImage.paste(pngImage,(0,0), pngImage)
jpgImage.save("london.jpg")
#print cairos.svg2png(file_obj=open('brockley_postcodes.svg','r'), dpi=100)

