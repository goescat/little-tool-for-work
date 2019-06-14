from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob
import sys

def parsefile(file):
    ##loading xml
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(file)

##Get file path from input argument
file_path = sys.argv[1]

try:
    ##load xml, if can correct loading print True
    parsefile(file_path)
    print "True"
except Exception, e:
    print "Error:", e
