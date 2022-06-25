#SVG : An SVG file is a graphics file that uses a two-dimensional graphic vector format 
#that defines images using an XML-based text format. 
# As a standard format for showing vector graphics on the web, SVG files are developed. 

# SVG = convert links into image formate

import pyqrcode
from pyqrcode import QRCode

# the link which need to be specified here 
l = "https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/"

# converting into QR 
url = pyqrcode.create(l)

# producing into QR image
url.svg("gnapathi.svg",scale = 8)
