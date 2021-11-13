def df(x):
    return x**2
def sp(x):
    return x**3/3 + 1

def euler( f, x0, y, h, ap ):
  
    # Iterating till the point at which we 
    # need approximation 
    while x0 < ap:
        y = y + h * f(x0) #change?
        x0 = x0 + h 
  
    # Printing approximation 
    print("Approximate solution at x = ", ap, " is ", "%.6f"% y)
    print('\n')
    print("Correct solution is: ", sp(5))
    print('\n')
    print ("Approximate error verified is: ", abs(y-sp(5)))

print(euler(df, 0, 1, 0.25, 5))

print("Second definition:", '\n')

# h= (xf-x0)/n, in this problem
    
def euler2(f, x0, y0, xf, n, h):
    for i in range(0, n):
        dy = f(x0)*h
        y0 += dy
        x0 += h
    print("Approximate solution at x = ", xf, " is ", "%.6f"% y0) 
    print('\n')
    print("Correct solution is: ", sp(5))
    print('\n')
    print ("Approximate error verified is: ", abs(y0-sp(5)))

def improved_euler(x0,y0,x1,y1, xf, n, f):
    xprev = x0
    yprev = y0
    x = x1
    y = y1
    h = (xf-x0)/n
    
    for i in range(n):
        ydern = f(x,y)
        p = yprev + 2*ydern*h
        pder = f(x+h, p)
        dyn = (pder + ydern)/2.0 * h 
        xprev = x
        yprev = y
        y = y + dyn
        x = x + h
        print(i, x, y, (x**2)/2.0)



print (euler2(df, 0, 1, 5, 20, 0.25))
    