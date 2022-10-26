import mymod

ans = int(input('Выберите действие:\n'
                '1. Просмотр справочника.\n'
                '2. Добавление записи в справочник.\n'
                '3. Поиск друга в справочнике.\n'
                'Введите номер пункта: '))
if ans == 1:
    mymod.view_friend()
elif ans == 2:
    mymod.add_friend()
else:
    mymod.find_friend()
