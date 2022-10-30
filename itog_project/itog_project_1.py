# 1) Ввести с клавиатуры N и M.
# Создать 2 таблицы данных в NumPy размера NxM - одну заполнить вручную, а вторую случайными числами.
# Найти сумму элементов всех массивов,
# Найти самый большой элемент массивов и самый маленький.
import numpy as np

# Задаём размерность таблиц
n = int(input('Введите N: '))
m = int(input('Введите М: '))
tab_1 = np.zeros((n, m))
# Заполнение и просмотр таблиц
for i in range(n):
    for j in range(m):
        tab_1[i, j] = int(input(f'Введите[{i} {j}] элемент таблицы: '))
print(f'Таблица № 1:\n {tab_1}')
tab_2 = np.random.randint(1, 100, (n, m))
print(f'Таблица № 2:\n {tab_2}')


# Поиск максимального элемента
def el_max():
    return np.max(tab_1) if np.max(tab_1) > np.max(tab_2) else np.max(tab_2)


# Поиск минимального элемента
def el_min():
    return np.max(tab_1) if np.max(tab_1) < np.max(tab_2) else np.max(tab_2)


# Сумма всех элементов
def el_sum():
    return tab_1.sum() + tab_2.sum()


print(f'Сумма всех элементов массивов - {el_sum()}')
print(f'Максимальный элемент массивов - {el_max()}')
print(f'Минимальный элемент массивов - {el_min()}')
