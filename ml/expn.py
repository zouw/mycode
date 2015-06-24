from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt


rv = expon(scale=5)
x=np.linspace(0, 20, 100)
plt.plot(x, rv.pdf(x))

plt.xlim([0, 15])
plt.title("exp dist")
plt.xlabel("RV")
plt.ylabel("f(x)")

plt.show()
