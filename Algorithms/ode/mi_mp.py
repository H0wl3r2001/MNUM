def D1(t):
    if(t>=0 and t<30):
        return 0
    elif(t >= 30 and t <= 90):
        return 0.002083*(t-30)
    elif(t > 90 and t<=749):
        return 0.002083*(90-30)/2**((t-90)/(4*60))

ka = 1.78895694153081099/60
ket = 0.154/60

def dMi(t, mi, mp):
    if(t<=750):
        return D1(t) - ka*mi
    

def dMp(t, mi, mp):
    if(t<=750):
        return ka*mi-ket*mp

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
        if process: print(f"    t = {x:<22} mi = {y:<22} mp = {z:<22}")
    return y, z

S = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 1)[1]
S1 = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 0.5)[1]
S2 = sup_rk4_method(dMi, dMp, 0, 90, 0, 0, 0.25)[1]

print(sup_rk4_method(dMi, dMp, 0, 224, 0, 0, 1))#(2.2402236923120857, 1.448595070403266), t = 90 / (1.562292526312284, 18.22207020861211), t = 467
print("QC (no minuto 90) =", (S2-S1)/(S1-S))