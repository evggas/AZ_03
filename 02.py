import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

print("Массив X:", x)
print("Массив Y:", y)

plt.scatter(x, y, color='blue', alpha=0.5)
plt.title("Диаграмма рассеяния для 5 случайных значений")
plt.xlabel("X - Случайные значения")
plt.ylabel("Y - Случайные значения")
plt.show()
