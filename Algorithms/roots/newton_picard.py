import math
def f(x):
    return (x*math.exp(-1.5*x)-0.154*math.exp(-0.154*1.5))
def fder(x):
    return (-1.5*x*math.exp(-1.5*x))


def D(t):
    if(t>=0 and t<30):
        return 0
    elif(t%750 >= 30 and t%750 <= 90):
        return 4/3*((t%750)-29)
    elif(t%750 > 90 and t%750<=749):
        return 40*0.9974361**((t%750)-29)


def newtons_method(function, derivative, guess): # also known as "método da tangente", derivative must be different than 0!
    before = 1e10
    while (abs(before - guess) > 1e-10):
        print(f"x = {guess:<22} f(x) = {function(guess):<22} f'(x) = {derivative(guess):<22}")
        before = guess
        guess = before - function(before)/derivative(before)
    return guess

def newton(f,Df,x0,prec,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn - xn) < prec:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

def Peano(g, gp, x0, epsilon):
    while True:
        if abs(gp(x0)) >= 1:
            print("Condicao necessaria nao encontrada")
            quit()
        med = g(x0)
        rel = abs((med-x0)/x0)
        x0 = med
        if rel <= epsilon:
            break
    return med

def picard_peano_function_annulment(x0, g, tolerance):
    x = x0
    while abs(f(x)) > tolerance:
        x = g(x)
    return x


print(newtons_method(f, fder, 1))
print(f(1.7889569415308109))
#print(newton(f,fder,1,1e-5,1000000))

#print (Peano(f, fder, 1, 1e-5))