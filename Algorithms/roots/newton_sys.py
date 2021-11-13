def f1(x, y):
    return ((x-4)*(x-4)+(y-4)*(y-4)-5)

def f2(x, y):
    return (x*x + y*y - 16)

def h(x,y):
    return -((2*x-8)*(f2(x,y))-2*x*(f1(x,y)))/(16*(x-y))
def k(x,y):
    return -((f1(x,y)*2*y-f2(x,y)*(2*y-8)))/(16*(x-y))


def g(x, y):
    for i in range (30):
       print(f1(x,y), f2(x,y))
       xn = x + k(x, y)
       yn = y + h(x, y)
       print (xn, yn)
       y = yn
       x = xn
       
print(g(3.4, 1.8))