from matplotlib import pyplot as plt
import numpy as np

x = 3.47
del_c = 0.25

c_values = np.arange(-10, 1, del_c)

l = (((abs(2 * x - c_values))**3)**(0.2)) + 0.567

for c, l_one in zip(c_values, l):
    print(f"a: {c:.2f}, f(с): {l_one:.2f}")

min_val = np.min(l)
max_val = np.max(l)
mean_val = np.mean(l)
array_size = len(l)
sorted_values = np.sort(l)

print(f"\nМинимальное значение: {min_val:.2f}")
print(f"Максимальное значение: {max_val:.2f}")
print(f"Среднее значение: {mean_val:.2f}")
print(f"Количество элементов: {array_size}")
print(f"Отсортированный массив:{sorted_values}")

plt.plot(c_values, l, label='f(с)')
plt.axhline(y=mean_val, color='y', linestyle='--', label='Среднее значение')
plt.xlabel('с')
plt.ylabel('f(с)')
plt.title('График')
plt.legend()
plt.grid(True) # сетка
plt.show()
