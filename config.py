class global_var:
    Func_List = {}

def add_func(name, f):
    global_var.Func_List[name] = f

def call_func(name, *args, **kwargs):
    return global_var.Func_List[name](*args, **kwargs)

def has_func(name):
    return name in global_var.Func_List
