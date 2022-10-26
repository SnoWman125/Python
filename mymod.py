def find_friend():
    try:
        with open('file7_spravochnik.txt', 'r', encoding='utf-8') as files:
            s = input('Введите данные об искомом друге: ')
            for file in files:
                if s in file:
                    print(file)
    except:
        print('File not found')


def add_friend():
    try:
        with open('file7_spravochnik.txt', 'a', encoding='utf-8') as files:
            files.write('\n' + input('Введите новую запись в формате "+7ХХХ... ФИО": '))
    except:
        print('File not found')


def view_friend():
    try:
        with open('file7_spravochnik.txt', 'r', encoding='utf-8') as files:
            s = files.readlines()
            print(s)
    except:
        print('File not found')
