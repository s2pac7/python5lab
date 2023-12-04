import numpy as np

a = 756.13
x = 0.3

print(((np.cos(x**2 + np.pi/6))**5 - np.sqrt(x * a**3) -
       np.log(abs((a - 1.12 * x) / 4))))
