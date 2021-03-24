from endprog import read_error
from readprog import readprog
#from parsing import parsing

if __name__ == "__main__":
    import sys
    from includes import library
    print(library.numequal(12, "12"))
    args = sys.argv
    if len(args) <= 1:
        read_error("no input files.")
    code = readprog(args[1])
    print(code)
 #   parsing(code)
