from sympy import symbols, simplify, Symbol

from sympy import sqrt as sym_sqrt
from sympy.vector import CoordSys3D

zero = Symbol("0")

def cp(a,b):
    N = CoordSys3D('N')
    v1 = a[0] * N.i + a[1] * N.j + a[2] * N.k
    v2 = b[0] * N.i + b[1] * N.j + b[2] * N.k

    return v1.cross(v2)

def magnitude(v):
    comps = v.components
    final = []
    for i in comps:
        final.append(comps[i])
    vx = final[0]**2
    vy = final[1] ** 2
    vz = final[2] ** 2
    return simplify(sym_sqrt(vx+vy+vz))

#create a variable for each thing you want to exist as an individual entity.
#if you want ax to be a times x, count them seperately, if you want ax to be its on indivisible thing, keep it as one
#you can name variables anything you want, but for ease of use i'd just name them whatever symbol they hold
#the only restricted symbol is "0" and variable name is zero
#example
ax = Symbol("ax")
bx = Symbol("bx")
ay = Symbol("ay")
by = Symbol("by")
az = Symbol("az")
bz = Symbol("bz")

t = Symbol("t")

#put the things you want to compute the cross product/magnitude of here.
# a and b are the two vectors you're taking the cross product of, with components entered in x y z order
#to multiply its *, power is **
#Example
a = [ax,ay,az]
b = [bx,bx,bz]

c = cp(a,b)

print(c)
print(magnitude(c))
