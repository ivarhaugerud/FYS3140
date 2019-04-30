import numpy as np
import matplotlib.pyplot as plt

N = int(1e6)
x = np.linspace(0, 4, N)
answ = np.zeros(N)

max = 100
a = np.linspace(0, max, int(max)+1)


answ2 = np.zeros(N, dtype="complex")
answ2 += 1
print(a)
for n in a:
    n = int(n)
    if n != 0:
        #answ2 += 1j()
        answ2 += -2*np.sin(n*np.pi*x)/(n*np.pi)
        #answ   += -1*(-1)**i*np.sin(i*np.pi*x)/np.pi
        #answ2 += 1j/(n*np.pi)*np.exp(1j*n*np.pi*x)*np.cos(n*np.pi)
        #answ2 += np.cos(2*np.pi*x*i)*np.cos(i*np.pi)/(i*i*np.pi*np.pi) #works +1/12

plt.plot(x, answ2)
plt.show()
