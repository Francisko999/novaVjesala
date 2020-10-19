def f():
    return 555
a=type("a",(),{
    "a":1,
    "b":2,
    "c":f})

#print(a.c())
class b:
    a=[]
    def __init__(self):
        self.aa=len(b.a)+10
        b.a.append(self)
    def b():
        return a

c=b()
cc=b()
ccc=b()
cccc=b()
print(b.a[0].aa)



g="f()"
try:
    print(2*eval(g))
except(NameError):
    pass
#getattr(main, g)()
c=6
def fun(a=0,b=0,c=0):
    print(a,b,c)
#x=[4,5,6]
x={"a":4,"b":5,"c":6}
fun(c=3,b=2)
fun(**x)
print(c)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#deklaracije i izvršavanje funkcije iz stringa
import inspect
lines = inspect.getsource(f)
#print(lines)
lines=lines[:4]+"h"+lines[5:]
print(lines)
exec(lines)
print(h())

lines = inspect.getsource(b)
lines=lines[:6]+"b2"+lines[7:]
exec(lines)
print(b.a)

