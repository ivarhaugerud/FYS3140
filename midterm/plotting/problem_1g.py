import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scpi
import seaborn as sns
import os

import matplotlib
matplotlib.rc('xtick', labelsize=16)
matplotlib.rc('ytick', labelsize=16)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'



def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = np.int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter



class Multiple:
    def __init__(self, denominator=2, number=np.pi, latex='\pi'):
        self.denominator = denominator
        self.number = number
        self.latex = latex

    def locator(self):
        return plt.MultipleLocator(self.number / self.denominator)

    def formatter(self):
        return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))


N = int(1e3)
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure(num=None, figsize=(14, 5), dpi=80, facecolor='w', edgecolor='k')
cbaxes = fig.add_axes([0.1, 0.1, 0.03, 0.8])  # This is the position for the colorbar

plt.subplot(1,3,1)
plt.title(r"$u = x$", fontsize=17)
eyy = plt.contourf(X, Y, X, 100)
cp = plt.contour(X, Y,  X, colors='black')
cp = plt.contour(X, Y, -X, colors='black')
plt.xlabel('$x$', fontsize=17)
plt.ylabel('$y$', fontsize=17)


plt.subplot(1,3,2)
plt.title(r"$v = y$", fontsize=17)
plt.contourf(X, Y, Y, 100)
cp = plt.contour(X, Y,  Y, colors='black')
cp = plt.contour(X, Y, -Y, colors='black')
plt.xlabel('$x$', fontsize=17)

plt.subplot(1,3,3)
plt.title(r"continous $u$ - dashed $v$", fontsize=17)
cp = plt.contour(X, Y, X)
cp = plt.contour(X, Y, Y, linestyles='dashed')
plt.xlabel('$x$', fontsize=17)
plt.tight_layout(pad=0.1, w_pad=0.1, h_pad=0.3)
plt.axis("equal")

plt.savefig("../figures/first.pdf", bbox_inches="tight")
os.system('pdfcrop %s %s &> /dev/null &'%("../figures/first.pdf", "../figures/first.pdf"))
plt.show()



plt.figure(num=None, figsize=(14, 5), dpi=80, facecolor='w', edgecolor='k')

plt.subplot(1,3,1)
plt.title(r"u = $x^2-y^2$", fontsize=17)
plt.contourf(X, Y, X**2-Y**2, 100)
cp = plt.contour(X, Y,  X**2-Y**2, colors='black')
cp = plt.contour(X, Y, -X**2+Y**2, colors='black')
plt.xlabel('$x$', fontsize=17)
plt.ylabel('$y$', fontsize=17)

plt.subplot(1,3,2)
plt.title(r"$v = 2xy$", fontsize=17)
plt.contourf(X, Y, X, 100)
cp = plt.contour(X, Y, -2*X*Y, colors='black')
cp = plt.contour(X, Y,  2*X*Y, colors='black')
plt.xlabel('$x$', fontsize=17)

plt.subplot(1,3,3)
plt.title(r"continous $u$ - dashed $v$", fontsize=17)
cp = plt.contour(X, Y, X**2-Y**2)
cp = plt.contour(X, Y, 2*X*Y, linestyles='dashed')
plt.xlabel('$x$', fontsize=17)
plt.tight_layout(pad=0.1, w_pad=0.1, h_pad=0.3)
plt.axis("equal")

plt.savefig("../figures/secound.pdf", bbox_inches="tight")
os.system('pdfcrop %s %s &> /dev/null &'%("../figures/secound.pdf", "../figures/secound.pdf"))

plt.show()


x = 2*np.linspace(-np.pi, np.pi, N)
y = 2*np.linspace(-np.pi, np.pi, N)
X, Y = np.meshgrid(x, y)

Z1 = np.sin(X)*np.cosh(Y)
Z2 = np.cos(X)*np.sinh(Y)

fig = plt.figure(num=None, figsize=(14, 5), dpi=80, facecolor='w', edgecolor='k')

plt.subplot(1,3,1)
plt.title(r"$u = \sin{x}\,\cosh{y}$", fontsize=17)
plt.contourf(X, Y, Z1, 100)
cp = plt.contour(X, Y,  Z1, colors='black')
cp = plt.contour(X, Y, -Z1, colors='black')
plt.xlabel('$x$', fontsize=17)
plt.ylabel('$y$', fontsize=17)

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
ax.yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

plt.subplot(1,3,2)
plt.title(r"$v = \cos{x}\,\sinh{y}$", fontsize=17)
plt.contourf(X, Y, Z2, 100)
cp = plt.contour(X, Y,  Z2, colors='black')
cp = plt.contour(X, Y, -Z2, colors='black')
plt.xlabel('$x$', fontsize=17)

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
ax.yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

plt.subplot(1,3,3)
plt.title(r"continous $u$ - dashed $v$", fontsize=17)
cp = plt.contour(X, Y, Z1)
cp = plt.contour(X, Y, Z2, linestyles='dashed')
plt.xlabel('$x$', fontsize=17)
limits = 0.9*2*np.pi
plt.axis("equal")
plt.axis([-limits, limits, -limits, limits])

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
ax.yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

plt.tight_layout(pad=0.1, w_pad=0.1, h_pad=0.1)
plt.savefig("../figures/third.pdf", bbox_inches="tight")
os.system('pdfcrop %s %s &> /dev/null &'%("../figures/third.pdf", "../figures/third.pdf"))

plt.show()
