#well the we can add extra features using decorators

def div(a,b):
    print(a/b)

def smart_div(fun):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return inner

div = smart_div(div)

div(10,5)

# read about the decoraters 

