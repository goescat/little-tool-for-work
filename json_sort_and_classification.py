#coding=utf-8
import os
import sys
import json
import fileinput
from collections import OrderedDict
from itertools import chain

##Get file path from cmd argument
file_path = sys.argv[1]

##Create file list for add .json file
file_list = []

for root, dirs, files in os.walk(file_path):  
    for filename in files:
        if ".json" in filename:
            file_list.append(filename)

##Sort file from file list
for filename in file_list:
    filepath_and_filename = file_path + "\\" + filename

    ##Open file with binary
    with open(filepath_and_filename, 'rb') as f:
        raw_data = f.read()
        ##decode with utf-8 and user json.loads to dictionary
        dict_ = json.loads(raw_data.decode('utf-8'))

    ##Create testcase and other method dictionary
    testcase_output = {}
    other_output = {}

    for key, value in dict_.iteritems():
        if "-" in key:
            ##save in testcase_output dict
            testcase_output[key] = value
        elif "-" not in key:
            ##save in other_output dict
            other_output[key] = value

    ##Use json.dumps to sort dict and to json
    testcase_output_json = json.dumps(testcase_output, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    other_output_json = json.dumps(other_output, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)

    ##Use json.loads to ordered dictionary to keep json order
    testcase_output_dict = json.loads(testcase_output_json, object_pairs_hook=OrderedDict)
    other_output_dict = json.loads(other_output_json, object_pairs_hook=OrderedDict)

    ##Merge 2 ordered dictionary
    output = OrderedDict(chain(testcase_output_dict.items(), other_output_dict.items()))

    ##Use json.dumps to json
    output_json = json.dumps(output, indent=4, separators=(', ', ': '), ensure_ascii=False)

    ##Write file
    with open(filename, 'ab') as f:
        f.write(output_json.encode('utf-8'))