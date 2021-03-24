import importlib
from endprog import runtime_error
from endprog import read_error
from includes.objects import obj
Func_List = {}
import_list = set()
def library_import(package, rename):
    module = 0
    try:
        module = importlib.import_module(package)
    except ImportError:
        read_error("No such file.")
    if rename in import_list:
        return
    library = getattr(module, "func_list")
    for key, val in library.items():
        if rename != "":
            new_name = rename + "." + key
        else:
            new_name = key
        if new_name in Func_List:
            runtime_error("Redefining " + new_name + ".")
        Func_List[new_name] = val
    import_list.add(rename)

def define_struct(struct_name, *args, **kwargs):
    arg = list(args)
    print(arg)
    for key in kwargs:
        arg.append(key)
    kwargs["ArGuMents"] = arg
    kwargs["Unbounded_Arg"] = len(args)
    kwargs["typename"] = struct_name
    New_class = type(struct_name, (obj,), kwargs)
    Func_List["make-" + struct_name] = lambda *args, **kwargs: New_class(*args, **kwargs)
    is_struct = Func_List[struct_name + "?"] = lambda x: type(x) is New_class
    for x in arg:
        def wrapper():
            att = x
            def getatt(y):
                if not is_struct(y):
                    runtime_error("Object " + y.__str__() + " is not type " + struct_name + ".")
                return getattr(y, att)
            return getatt
        Func_List[struct_name + "-" + x] = wrapper()



def parsing(code):
    pass

if __name__ == "__main__":
    library_import("includes.library", "")
    print(Func_List["list"](12, 23))
    define_struct("Hello", "a", "b", "c", d = 45)
    x = Func_List["make-Hello"](12, 23, 34)
    print(getattr(x, "a"))
    print(Func_List["Hello-a"](x))
    print(getattr(x, "b"))
    print(Func_List["Hello-b"](x))
    print(getattr(x, "c"))
    print(Func_List["Hello-c"](x))
    print(getattr(x, "d"))
    print(Func_List["Hello-d"](x))
    Func_List["display"](x)
