#coding=utf-8
import os
import sys
import json
import fileinput
from collections import OrderedDict
from itertools import chain

file_path = sys.argv[1]

with open(file_path, 'rb') as f:
    raw_data = f.read()
    dict_ = json.loads(raw_data.decode('utf-8'))

testcase_output = {}
other_output = {}

for key, value in dict_.iteritems():
    # if a character is in a string.
    if "-" in key:
        testcase_output[key] = value
        # print output
    if "-" not in key:
        other_output[key] = value
        # print output

testcase_output_json = json.dumps(testcase_output, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
other_output_json = json.dumps(other_output, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)

testcase_output_dict = json.loads(testcase_output_json, object_pairs_hook=OrderedDict)
other_output_dict = json.loads(other_output_json, object_pairs_hook=OrderedDict)

output = OrderedDict(chain(testcase_output_dict.items(), other_output_dict.items()))
# print output

output_json = json.dumps(output, indent=4, separators=(', ', ': '), ensure_ascii=False)

# print output
file_name = os.path.basename(file_path)

with open(file_name, 'ab') as f:
    f.write(output_json.encode('utf-8'))