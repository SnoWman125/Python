# 1) Вводим строчку и меняем все пробелы на знак подчеркивания

s = input('Введите строку: ')
s = s.replace(' ', '_')
print(s)
# s_new = ''
# i = 0
# while i < len(s):
#     s_new += s[i] if s[i] != ' ' else '_'
#     i += 1
# print(s_new)

# 2) Вводим строчку и выводим на экран:
# * общее количество символов в строке;
# * каждый чётный символ,
# * все символы в обратном порядке

s = input('Введите строку: ')
new_s = ''
l = len(s)
print(s)
print(f'Общее количество символов: {l}')
print(s[1::2])
print(s[::-1])

# 3) Вводим строчку и выводим разницу между количеством букв в верхнем и нижнем регистре.
s = input('Введите строку: ')
i = 0
count_Up = 0
while i < len(s):
    if s[i].istitle():
        count_Up += 1
    i += 1
count = len(s) - count_Up
if count > count_Up:
    raz = count - count_Up
else:
    raz = count_Up - count
print(f'Разность между количеством букв в верхнем и нижнем регистре: {raz}')
