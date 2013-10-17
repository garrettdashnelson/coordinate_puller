from pykml import parser

file = raw_input('Enter the file name: ')

doc = parser.parse(file).getroot()

for el in doc.Document.Placemark:
	if el.find("LineString") is not None:
		for s in el.LineString:
			print s.coordinates.text
	if el.find("Point") is not None:
		for s in el.Point:
			print s.coordinates.text
