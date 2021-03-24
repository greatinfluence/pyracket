import sys
def endprog(Error_Info = "", Type = 0):
    print(Error_Info)
    sys.exit(Type)

def read_error(Error_Info):
    endprog(Error_Info, Type = 1)

def runtime_error(Error_Info):
    endprog(Error_Info, Type = 2)
