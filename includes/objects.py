from endprog import runtime_error
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

class Pair(obj):
    __slots__ = ['x', 'y']
    ArGuMents = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if type(self.y) is empty or type(self.y) is Pair:
            s = "(list " + str(self.x)
            cur = self
            while type(cur.y) is Pair:
                cur = cur.y
                s = s + " " + str(cur.x)
            s = s + ")"
            return s
        else:
            return "(cons " + str(self.x) + " " + str(self.y) + ")"

class empty(obj):
    typename = "empty"
    def __str__(self):
        return "'()"

Empty = empty()
