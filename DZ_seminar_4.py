# ДЗ 1
# 1) Создать список случайных чисел от -10, до 10 на num * 2 элементов. num вводим с клавиатуры.
from random import randint

num = int(input('Введите num: '))
arr = []
for i in range(num * 2):
    arr.append(randint(-10, 10))
print(arr)
# 2) Вывести все числа меньше 0 и делящиеся на 3
arr_2 = []
for i in arr:
    if i < 0 and i % 3 == 0:
        arr_2.append(i)
print(arr_2)
# 3) Сказать кол-во элементов 5 и 3
count = 0
for i in arr:
    if i == 5 or i == 3:
        count += 1
print(f'Количество 3 и 5: {count} штук')
# 4) Вывести разницу между кол-вом максимальных и минимальных значений
min = min(arr)
max = max(arr)
count_min = 0
count_max = 0
for i in arr:
    if i == min:
        count_min += 1
    elif i == max:
        count_max += 1
if count_max > count_min:
    raz = count_max - count_min
else:
    raz = count_min - count_max
print(f'Макс - {max} в кол-ве {count_max}, Мин - {min} в кол-ве {count_min}. Разность - {raz}')
# 5) Сделать копию списка. Равзернуть и упорядочить список список
arr_5 = arr
arr_5.reverse()
print(arr_5)
arr_5.sort()
print(arr_5)
# 6) Удалить половину элементов списка
half = int(len(arr) / 2)
for i in range(half):
    arr.pop(i)
print(arr)
# 7) Очистить список
arr.clear()
print(arr)

# ДЗ 2
# Сгенерировать список на num элементов от 150 до 200. num вводим с клавиатуры.
# Мы вводим с клавиатуры какое-то число в этом диапазоне ( от 150 до 200).
# Это построение по росту в строю. Необходимо поставить в строй введеный лемент
# Например: сгенерировались 163, 175, 169, 200
# Вбили с клавиатуры 180
# Вы второй в строю. И вывести список.
num = int(input('ВВедите количество элементов: '))
arr = []
for i in range(num):
    arr.append(randint(150, 200))
print(arr)
arr.sort(reverse=True)
print(arr)
x = int(input('Введите рост: '))
for i in range(len(arr) - 1):
    if x > arr[i]:
        arr.insert(i, x)
        break
    else:
        arr.append(x)
        break
print(arr)
