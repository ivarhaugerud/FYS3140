import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scpi
import seaborn as sns
import os

import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

N = int(1e3)
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)

plt.figure(1)
plt.contourf(X, Y, Y, 100)
plt.colorbar();
cp = plt.contour(X, Y,  Y, colors='black')
cp = plt.contour(X, Y, -Y, colors='black')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.show()

plt.figure(2)
plt.contourf(X, Y, X, 100)
plt.colorbar();
cp = plt.contour(X, Y,  X, colors='black')
cp = plt.contour(X, Y, -X, colors='black')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.show()

plt.figure(3)
cp = plt.contour(X, Y, X, colors='black')
cp = plt.contour(X, Y, -X, colors='black')
cp = plt.contour(X, Y, Y, colors='red')
cp = plt.contour(X, Y, -Y, colors='red')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.show()


Z1 = np.cos(X)*np.sinh(Y)
Z2 = np.sin(X)*np.cosh(Y)

plt.figure()
cp = plt.contour(X, Y, Z1, colors='black')
cp = plt.contour(X, Y, -Z1, colors='black')
plt.contourf(X, Y, Y, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar();
plt.show()

plt.figure()
cp = plt.contour(X, Y, Z2)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.colorbar();
plt.show()

plt.figure()
cp = plt.contour(X, Y, Z1, colors='black')
cp = plt.contour(X, Y, Z2, colors='red')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()
