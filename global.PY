import math
def gcd(a,b):
    g=(math.gcd(a,b))
    print(g)

gcd(12,13)
#global
global var
vat="hello"

def f():
    vat="new value"
    print(vat)
f()
print(vat)
global k
k=235
def chance():
    global k
    k=2536
chance()
print(k)

global lst

lst = 123

def change():
  global lst
  lst = 234

change()
print(lst)
