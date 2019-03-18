import os
import sys
import json
import fileinput

file_path = sys.argv[1]
file = open(file_path, 'r')
content = file.read()

content = json.dumps(json.loads(content), sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False).encode('utf8')
# print content
file_name = os.path.basename(file_path)

sort_file = open(file_name, 'a')
sort_file.write(content)
sort_file.close()