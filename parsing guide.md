```python
import functools
parsing_error = functools.partial(endprog, Type = 2)
```



parsing:

Read Left parenthesis, then it must be a function.

```lisp
((lambda (x) (add1 x)) x)
```

Some functions needed to be accomplished in python:

define, define-struct, local, let, set!, display, lambda

define , lambda and set! need to be written in the parsing part.

```python
class obj:
    typename = "object"
    ArGuMents = []
    Unbounded_Arg = 0
    
    def __str__(self):
        return "#<procedure:" + self.typename + ">"
    
    def __init__(self, *args, **kwargs):
        if len(args) < self.Unbounded_Arg:
            runtime_error("Too little arguments for " + self.typename + ".")
        if len(args) > len(self.ArGuMents):
            runtime_error("Too much arguments for " + self.typename + ".")
        for (x, y) in zip(self.ArGuMents, args):
            setattr(self, x, y)
        for x, y in kwargs:
            setattr(self, x, y)

    def __getattr__(self, name):
        runtime_error(self.typename + "has no attribute " + name + ".")
        

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



def display(x):
    print(x)
```



Parsing:

First, we need to combine the libraries.

```python
import importlib
func_list = {}
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
        if new_name in func_list:
            runtime_error("Redefining " + new_name + ".")
        func_list[new_name] = val
    import_list.add(rename)
```

```python
def translate_to_python(code):
    code = code.expandtabs(tabsize = 4)
    in_string = False
    in_comment = False
    in_symbol = False
   	string = []
   	escaped = False
    python_code = []
    for i in code:
        if in_comment:
            if i == '\n':
                in_comment = False
            continue
        if escaped:
            string.append(i)
            escaped = False
        if i == '\"':
            if in_string:
                string.append('\"')
                python_code.append("".join(string))
                string = []
                in_string = False
            else:
                if in_symbol:
                    in_symbol = False
                    # starting from here
                in_string = True
                string.append('\"')
            continue
        if in_string:
            if i == '\\':
            	escaped = True
            string.append(i)
            continue
        if i == ';':
            in_comment = True
            continue
        if i == '(':
            
        
```

```lisp
(((((lambda (x) (lambda (x) (lambda (x) add1))) 12) 12) 12) 12)
```

```python
(lambda x : lambda x : lambda x : lambda x : x + 1)(12)(12)(12)(12)
```



Dynamic parsing in Python:

```python
from types import FunctionType
foo_code = compile(code, "<string>", "exec")
foo_func = FunctionType(foo_code.co_consts[0], globals(), name)
```



Dynamic importing in Python:

```python
import importlib
module = importlib.import_module('filename.module')
```



Dynamic creating classes in Python:

```python
dic = kwargs
for k in args:
    if k in dic:
        endprog(Error_Info = "Redefining argument " + k + ".", Type = 2)
        
New_Class = type(Func_name, (inherites, ), dict(*args))
```



Found the usage of a function:

```python
from inspect import signature
signature(func_name)
```



Dynamic call function:

```python
getattr(module, func_name)(args)
```



