import sys
import os

def pycodestyle_validation(file_path):
    ##Execute pycodestyle
    pycodestyle_cfg_path = os.getcwd() + r"data\Common\codestyle.cfg"
    command = "pycodestyle " + file_path + " --config='" + pycodestyle_cfg_path + "'"
    result = os.popen(command).read()

    if result == "":
        print "True"
    else:
        print "Error: ", result

##Get file path from input argument
file_path = sys.argv[1]
pycodestyle_validation(file_path)
