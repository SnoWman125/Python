# 1.1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный
# Добавьте возможность использования скобок, меняющих приоритет операций.
s = '(2+2)*3'
print(eval(s))

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

arr = [1, 1, 2, -1, 2, 3, 1, 4, 2, 5]
new = []
for i in arr:
    if arr.count(i) > 1:
        continue
    else:
        new.append(i)
print(new)