from pykml import parser

file = raw_input('Enter the file name: ')

doc = parser.parse(file)

for elt in doc.findall('//coordinates'):
	print elt.text