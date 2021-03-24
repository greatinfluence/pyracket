from endprog import runtime_error
from includes.objects import Pair, Empty, obj
from config import add_func

def plus(x, *args):
    for y in args:
        x = x + y
    return x

def minus(x, *args):
    for y in args:
        x = x - y
    return x

def mult(x, *args):
    for y in args:
        x = x * y
    return x

def divi(x, *args):
    for y in args:
        x = x / y
    return x

def quotient(x, y):
    return x // y

def modulo(x, y):
    return x % y

def equal(f, x, *args):
    if not f(x):
        runtime_error("The parameters do not suite the limits of this function.")
    for y in args:
        if not f(y):
            runtime_error("The parameters do not suite the limits of this function.")
        if x != y:
            return False
    return True

def Equal(x, *args):
    return equal(lambda x : True, x, args)

def numequal(x, *args):
    return equal(lambda x : type(x) is int or type(x) is float, x, args)

def strequal(x, *args):
    return equal(lambda x : type(x) is str, x, args)

def cons(x, y):
    return Pair(x, y)

def List(*args):
    curlist = Empty
    for i in args[: : -1]:
        curlist = Pair(i, curlist)
    return curlist

def define_struct(struct_name, *args, **kwargs):
    arg = list(args)
    for key in kwargs:
        arg.append(key)
    kwargs["ArGuMents"] = arg
    kwargs["Unbounded_Arg"] = len(args)
    kwargs["typename"] = struct_name
    New_class = type(struct_name, (obj,), kwargs)
    add_func("make-" + struct_name, lambda *args, **kwargs: New_class(*args, **kwargs))
    is_struct = lambda x: type(x) is New_class
    add_func(struct_name + "?", is_struct)
    for x in arg:
        def getat():
            att = x
            def getatt(y):
                if not is_struct(y):
                    runtime_error("Object " + y.__str__() + " is not type " + struct_name + ".")
                return getattr(y, att)
            return getatt
        add_func(struct_name + "-" + x, getat())
        def setat():
            att = x
            def setatt(y, val):
                if not is_struct(y):
                    runtime_error("Object " + y.__str__() + " is not type " + struct_name + ".")
                setattr(y, att, val)
            return setatt
        add_func("set-" + struct_name + "-" + x + "!", setat())

func_list = {"+" : plus, "-" : minus, "*" : mult, "/" : divi
        , "quotient" : quotient, "modulo" : modulo
        , "remainder" : modulo, "cons" : cons
        , "list" : List, "=" : numequal, "equal?" : Equal
        , "string=?" : strequal, "display" : print
        , "define-struct" : define_struct}
