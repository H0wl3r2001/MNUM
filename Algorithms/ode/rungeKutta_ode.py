import numpy as np
def df(x, y):
    return x**2

def sp(x, y):
    return x**3/3 + 1

def rungeKutta2(f, x0, y0, x, h, n) :   
    y = y0;  
      
    for i in range(0, n) : 
          
        # Apply Runge Kutta Formulas  
        # to find next value of y  
        k1 = h * f(x0, y);  
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1);  
  
        # Update next value of y  
        y += k2  
  
        # Update next value of x  
        x0 = x0 + h;  
  
    return y;

def D1(t):
    if(t>=0 and t<30):
        return 0
    elif(t >= 30 and t <= 90):
        return 0.002083*(t-30)
    elif(t > 90 and t<=749):
        return 0.002083*(90-30)/2**((t-90)/(4*60))
    

def D(t):
    if(t>=0 and t<30):
        return 0
    elif(t >= 30 and t <= 90):
        return 0.003359*2/3*(t-30)
    elif(t > 90 and t<=749):
        return 0.003359*40*0.9974361**(t-30)


ka = 1.789/60
ket = 0.154/60

def dMi(t, mi, mp):
    if(t<=750):
        return D1(t) - ka*mi
    

def dMp(t, mi, mp):
    if(t<=750):
        return ka*mi-ket*mp

def RK2nd(yp, zp, x0, xf, y0, z0, h):
    y = y0
    z = z0
    while(round(x0, 2)<xf):
        ya = y
        y = y + h*yp(x0+h/2, y + (h/2)*yp(x0, y, z), z+(h/2)*zp(x0, y, z))
        z = z + h*zp(x0+h/2, ya + (h/2)*yp(x0, ya, z), z+(h/2)*zp(x0, ya, z))
        x0 += h
    return (y, z)

def RK4th(x,y,z,xf,n):
    h = (xf-x)/n
    for _ in range(n):
        dy1 = h*dMi(x,y,z)
        dz1 = h*dMp(x,y,z)
        dy2 = h*dMi(x+h/2,y+dy1/2,z+dz1/2)
        dz2 = h*dMp(x+h/2,y+dy1/2,z+dz1/2)
        dy3 = h*dMi(x+h/2,y+dy2/2,z+dz2/2)
        dz3 = h*dMp(x+h/2,y+dy2/2,z+dz2/2)
        dy4 = h*dMi(x+h,y+dy3,z+dz3)
        dz4 = h*dMp(x+h,y+dy3,z+dz3)
        x1 = x + h
        y1 = y + (1/6)*dy1 + (1/3)*dy2 + (1/3)*dy3 + (1/6)*dy4
        z1 = z + (1/6)*dz1 + (1/3)*dz2 + (1/3)*dz3 + (1/6)*dz4
        x = x1
        y = y1
        z = z1
    return (y,z)

def sup_rk4_method(diff_y, diff_z, initial_x, final_x, initial_y, initial_z, h, process = True):
    if process: print("Superior Rk4's method:")
    x = initial_x; y = initial_y; z = initial_z
    for _ in range(round((final_x-initial_x)/h)):
        temp = [0]*8
        temp[0] = h * diff_y(x,y,z)
        temp[4] = h * diff_z(x,y,z)
        temp[1] = h * diff_y(x+h/2, y+temp[0]/2, z+temp[4]/2) 
        temp[5] = h * diff_z(x+h/2, y+temp[0]/2, z+temp[4]/2) 
        temp[2] = h * diff_y(x+h/2, y+temp[1]/2, z+temp[5]/2) 
        temp[6] = h * diff_z(x+h/2, y+temp[1]/2, z+temp[5]/2)
        temp[3] = h * diff_y(x+h, y+temp[2], z+temp[6])
        temp[7] = h * diff_z(x+h, y+temp[2], z+temp[6])
        y += (temp[0]/6 + temp[1]/3 + temp[2]/3 + temp[3]/6)
        z += (temp[4]/6 + temp[5]/3 + temp[6]/3 + temp[7]/6)
        x += h
        if process: print(f"    x = {x:<22} y = {y:<22} z = {z:<22}")
    return y, z

S = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 1)[1]
S1 = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 0.5)[1]
S2 = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 0.25)[1]

print(sup_rk4_method(dMi, dMp, 30, 90, 0, 0, 1))
print("QC =", (S2-S1)/(S1-S))

#xf = 5
#print("Approximate solution at xf=",xf, "is:", rungeKutta(df, 0, 1, 5, 0.125, 40), '\n')
#print("Correct solution is: ", sp(5,0), '\n')
#print(print ("Approximate error verified is: ", abs(rungeKutta(df, 0, 1, 5, 0.5, 10)-sp(5,0))))

