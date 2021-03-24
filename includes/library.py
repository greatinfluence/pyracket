from endprog import runtime_error
from includes.objects import Pair, Empty

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

func_list = {"+" : plus, "-" : minus, "*" : mult, "/" : divi
        , "quotient" : quotient, "modulo" : modulo
        , "remainder" : modulo, "cons" : cons
        , "list" : List, "=" : numequal, "equal?" : Equal
        , "string=?" : strequal, "display" : print}
