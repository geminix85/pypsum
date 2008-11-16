#!/usr/bin/env python

import urllib2
import xml.sax

def get_lipsum(howmany, what, start_with_lipsum):
	
	class XmlHandler(xml.sax.handler.ContentHandler):
		
		def __init__(self):
			self.lipsum = ''
			self.generated = ''
		
		def startElement(self, name, attrs):
			self.current_tag = name
		
		def endElement(self, name):
			self.current_tag = None
		
		def characters(self, content):
			if self.current_tag == 'lipsum':
				self.lipsum += content
			elif self.current_tag == 'generated':
				self.generated += content
	
	query_str  = "amount=" + str(howmany)
	query_str += "&what=" + what
	query_str += "&start=" + start_with_lipsum
	
	f = urllib2.urlopen("http://www.lipsum.com/feed/xml", query_str)
	
	handler = XmlHandler()
	parser = xml.sax.make_parser()
	parser.setContentHandler(handler)
	parser.parse(f)
	
	f.close()
	
	return handler.lipsum, handler.generated

get_lipsum.__doc__ = """Get lorem ipsum text from lipsum.com. Parameters:
howmany: how many items to get
what: the type of the items [paras/words/bytes/lists]
start_with_lipsum: whether or not you want the returned text to start with Lorem ipsum [yes/no]
Returns a tuple with the generated text on the 0 index and generation statistics on index 1"""

if __name__ == "__main__":
	import sys
	if len(sys.argv) != 4:
		print """Usage: pypsum howmany what start_with_lipsum
	howmany: how many items to get
	what: the type of the items. Can be: paras/words/bytes/lists
	start_with_lipsum: whether or not the text should start with "Lorem ipsum" [yes/no]"""
	else:
		lipsum = get_lipsum(sys.argv[1], sys.argv[2], sys.argv[3])
		print lipsum[0] + "\n\n" + lipsum[1]

