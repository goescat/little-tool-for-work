import sys
import json

def json_validation(data):
    ##load json, if can correct loading print True
    try:
        json.loads(data)
        print "True"
    except ValueError as e:
        print "Error: ", e

##Get file path from input argument
file_path = sys.argv[1]

file = open(file_path, 'r')
json_content = file.read()
json_validation(json_content)
