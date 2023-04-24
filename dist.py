from sympy import Symbol, sqrt


def dist(a, b):
    c = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    return c


def semiperimiter(a,b,c):
    d = dist(a,b) + dist(a,c) + dist(b,c)
    return d

def huron(a,b,c):
    da = dist(a,b)
    print("L_1: " + str(da))
    db = dist(b,c)
    print("L_2: " + str(db))
    dc = dist(c,a)
    print("L_3: " + str(dc))
    s = semiperimiter(a,b,c)
    print("S: " + str(s))
    return sqrt(s*(s-da)*(s-db)*(s-dc))


a = [Symbol("A_x"),Symbol("A_y"),Symbol("A_z")]
b = [Symbol("B_x"),Symbol("B_y"),Symbol("B_z")]
c = [Symbol("C_x"),Symbol("C_y"),Symbol("C_z")]

print(huron(a,b,c))

