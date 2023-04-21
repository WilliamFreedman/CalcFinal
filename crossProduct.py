from sympy import symbols, simplify, Symbol

from sympy import sqrt as sym_sqrt
from sympy.vector import CoordSys3D, cross
import numpy as np
from math import sqrt


def cross_product(a,b):
    ax, ay, az, bx, by, bz = symbols(" ".join(a+b))
    a2 = np.array([ax,ay,az])
    b2 = np.array([bx,by,bz])
    return np.cross(a2,b2)

def cp(a,b):
    N = CoordSys3D('N')
    ax = Symbol("(" + a[0] + ")")
    ay = Symbol("(" + a[1] + ")")
    az = Symbol("(" + a[2] + ")")
    bx = Symbol("(" + b[0] + ")")
    by = Symbol("(" + b[1] + ")")
    bz = Symbol("(" + b[2] + ")")

    v1 = ax * N.i + ay * N.j + az * N.k
    v2 = bx * N.i + by * N.j + bz * N.k

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


#put the things you want to compute the cross product/magnitude of here. No spaces.
a = ["ax-y","ab+c","ax-q"]
b = ["ax+4","ax+6","ax-1"]

c = cp(a,b)

print(c)
print(magnitude(c))
