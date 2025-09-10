import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import dual_annealing

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html#scipy.optimize.dual_annealing

func = lambda x: 20 * x**2 + x + 5

t = np.linspace(-100, 100, 100)
plt.plot(t, func(t))
plt.show()

lw = [-100]
up = [100]
ret = dual_annealing(func, bounds=list(zip(lw, up)))
print(ret.x)
