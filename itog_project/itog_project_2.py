# 2) Создать таблицу данных в pandas - заполнить
# Добавить новый столбец.
import pandas as pd

data = {'car': ['mazda', 'toyota', 'subaru', 'mercedes', 'audi'],
        'color': ['black', 'red', 'yellow', 'blue', 'white'],
        'price': [80, 120, 90, 180, 170]}
frame = pd.DataFrame(data)
frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)

# Добавление нового столбца
frame['isSold'] = False

print(frame)
