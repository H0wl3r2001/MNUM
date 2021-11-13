import math

def f(x):
    return (x*math.exp(-1.5*x)-0.154*math.exp(-0.154*1.5))
def fder(x):
    return (-1.5*x*math.exp(-1.5*x))

def newtons_method(function, derivative, guess): # also known as "método da tangente", derivative must be different than 0!
    before = 1e10
    while (abs(before - guess) > 1e-10):
        print(f"x = {guess:<22} f(x) = {function(guess):<22} f'(x) = {derivative(guess):<22}")
        before = guess
        guess = before - function(before)/derivative(before)
    return guess

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
        s = (a*f(b) - b*(f(a)/2))/(f(b)-(f(a)/2))
        if (f(a)*f(s)<=0):
            b=s
        else:
            a=s
        c += 1
    print(c)
    print(a)
    print(b)
    print(s)
    return (a+b)/2

print("Bisseçao:", bissec(1, 2, 0.001)) #1.78857421875
print("Newton's method:", newtons_method(f, fder, 1)) #1.78895694153081099
#print(cord(1,2,0.1))
