from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
z2 = x**2 + y**2
z3 = 2*x + 3*y
z4 = x**2 - y**2
z5 = 2 + 2*x + 2*y - x**2 - y**2

fig = plt.figure(figsize=(15, 10))

ax1 = fig.add_subplot(151, projection='3d')
ax1.plot_surface(x, y, z1, cmap='inferno')
ax1.set_title('1-й график')

ax2 = fig.add_subplot(152, projection='3d')
ax2.plot_surface(x, y, z2, cmap='inferno')
ax2.set_title('2-й график')

ax3 = fig.add_subplot(153, projection='3d')
ax3.plot_surface(x, y, z3, cmap='inferno')
ax3.set_title('3-й график')

ax4 = fig.add_subplot(154, projection='3d')
ax4.plot_surface(x, y, z4, cmap='inferno')
ax4.set_title('4-й график')

ax5 = fig.add_subplot(155, projection='3d')
ax5.plot_surface(x, y, z5, cmap='inferno')
ax5.set_title('5-й график')

plt.show()