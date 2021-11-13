import math

def f(x):
    return x*math.exp(-1.5*x)-0.154*math.exp(-1.5*0.154)
def f1(x):
    return x*math.exp(-1.5*x)-0.154*math.exp(-1.5*0.154)
  
def bissec(a, b, p):
    c=0
    while (abs(b-a) > p):
        m = (b+a)/2
        if (f(a)*f(m)<=0):
            b=m
        else:
            a=m
        c += 1
    print(c)
    print(a)
    print(b)
    print(m)        
    return (a+b)/2

def cord(a, b, p):
    c = 0
    while (abs(b-a) > p):
        s = (a*f1(b) - b*(f1(a)/2))/(f1(b)-(f1(a)/2))
        if (f1(a)*f1(s)<=0):
            b=s
        else:
            a=s
        c += 1
    print(c)
    print(a)
    print(b)
    print(s)
    return (a+b)/2

print(bissec(1, 2, 0.001))
print("absolute error:", (2-1)/2**7)
print("relative error:", ((2-1)/2**7)/bissec(1, 2, 0.001))

#print("Now, the other method")

#print(cord(1, 2, 0.1))
#print(math.sqrt(3))