import matplotlib.pyplot as plt
import numpy as np

def D1(t):
    if(t>=0 and t<30):
        return 0
    elif(t >= 30 and t <= 90):
        return 0.002083*(t-30)
    elif(t > 90 and t<=749):
        return 0.002083*(90-30)/2**((t-90)/(4*60))

tcords = []
ycords = []

for t in np.linspace(0, 750, 1500):
    y = D1(t)
    tcords.append(t)
    ycords.append(y)

plt.plot(tcords, ycords)
plt.xlabel('tempo (minutos)')
plt.ylabel('massa do medicamento administrado (mg)')
plt.show()
#for i in range(750):
    #print(D(i))
