import os
from endprog import read_error
def readprog(path):
    if not os.path.isfile(path):
        read_error("No such file.")
    code = ""
    with open(path, "r") as f:
        code = f.read()
    return code
