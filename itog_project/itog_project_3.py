# 3) Построить график y = 1\x
# Настроить внешний вид таблицы.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
y = [1 / i for i in x]
print(x)
plt.plot(x, y, color='red', linestyle='--')
plt.title('y = 1/x')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
