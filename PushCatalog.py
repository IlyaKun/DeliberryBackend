import csv
import json
import subprocess
import os
from datetime import datetime

# Укажите путь к вашему CSV файлу
csvFile = '/Users/ila/Documents/GitDeliberry/Catalog.csv'
# Укажите путь для сохранения JSON файла
jsonFile = '/Users/ila/Documents/GitDeliberry/CatalogJSON.json'



# Список необходимых ключей
required_keys = [
    "Tilda_UID",
    "Mark",
    "Category",
    "Title",
    "Description",
    "Text",
    "Photo",
    "Price",
    "Price_Old",
    "Editions",
    "External_ID",
    "Parent_UID"
]

# Чтение данных из CSV файла с использованием точки с запятой в качестве разделителя
with open(csvFile, mode='r', encoding='utf-8') as file:
    csvReader = csv.DictReader(file, delimiter=';')  # Указываем delimiter как ';'
    
    # Преобразуем данные в список словарей с измененными ключами
    data = []
    for row in csvReader:
        new_row = {}
        for key, value in row.items():
            # Заменяем пробелы на нижние подчеркивания в ключах
            new_key = key.replace(' ', '_')
            # Проверяем, входит ли новый ключ в список необходимых ключей
            if new_key in required_keys:
                new_row[new_key] = value
        
        # Проверяем, что новый словарь содержит 12 ключей
        if len(new_row) != len(required_keys):
            print(f"Ошибка: элемент не содержит {len(required_keys)} ключей. Программа завершена.")
            sys.exit(1)  # Завершение программы с кодом ошибки

        data.append(new_row)

# Запись данных в JSON файл
with open(jsonFile, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Используем indent для форматирования

# Получение текущей даты и времени
current_time = datetime.now().strftime('%d.%m.%y %H:%M:%S')

# Комментарий к коммиту с добавлением текущей даты и времени
commit_message = f'Updated JSON file {current_time}'

# Отправка изменений в Git
subprocess.run(['git', 'add', "."])
subprocess.run(['git', 'commit', '-m', commit_message])
subprocess.run(['git', 'push'])
