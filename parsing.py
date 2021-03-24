import importlib
from endprog import runtime_error
from endprog import read_error
from includes.objects import obj
from config import call_func, has_func, add_func
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
        if has_func(new_name):
            runtime_error("Redefining " + new_name + ".")
        add_func(new_name, val)
    import_list.add(rename)
'''
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
        def getat():
            att = x
            def getatt(y):
                if not is_struct(y):
                    runtime_error("Object " + y.__str__() + " is not type " + struct_name + ".")
                return getattr(y, att)
            return getatt
        Func_List[struct_name + "-" + x] = getat()
        def setat():
            att = x
            def setatt(y, val):
                if not is_struct(y):
                    runtime_error("Object " + y.__str__() + " is not type " + struct_name + ".")
                setattr(y, att, val)
            return setatt
        Func_List["set-" + struct_name + "-" + x + "!"] = setat()
'''


def parsing(code):
    pass

if __name__ == "__main__":
    library_import("includes.library", "")
    print(call_func("list", 12, 23))
    call_func("define-struct", "Hello", "a", "b", "c", d = 45)
    x = call_func("make-Hello", 12, 23, 34)
    print(call_func("Hello-a", x))
    call_func("display", x)
    call_func("set-Hello-a!", x, "Hello!")
    call_func("display", x)

