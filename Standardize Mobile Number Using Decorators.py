#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        l = sorted(["+91 " + x[-10:-5] + " " + x[-5:] for x in l])
        return f(l)
    return fun