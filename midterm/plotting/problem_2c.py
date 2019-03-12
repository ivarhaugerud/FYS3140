import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use("bmh")
sns.color_palette("hls", 1)

import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

N = int(1e5)
x = np.linspace(-3, 3, N)

plt.plot(x, x**2)
#plt.plot(x, np.cosh(x**2)-1)
#plt.axis([-3, 3, -0.1, 9])

plt.legend(loc="best", fontsize=13)
plt.xlabel(r"$x$   $\left[\frac{n_0\gamma}{2K}(x-x_0)\right]$", fontsize=14)
plt.ylabel(r"$y - \frac{K-n_0}{\gamma n_0}$   $\left[\frac{n_0\gamma}{2K}\right]$", fontsize=14)

plt.savefig("../figures/2c.pdf", bbox_inches = "tight")
os.system('pdfcrop %s %s &> /dev/null &'%("../figures/2c.pdf", "../figures/2c.pdf"))
plt.show()
