import csv
import json
import subprocess
import os
from datetime import datetime

# Укажите путь к вашему CSV файлу
csvFile = '/Users/ila/Documents/GitDeliberry/Catalog.csv'
# Укажите путь для сохранения JSON файла
jsonFile = '/Users/ila/Documents/GitDeliberry/CatalogJSON.json'



# Чтение данных из CSV файла с использованием точки с запятой в качестве разделителя
with open(csvFile, mode='r', encoding='utf-8') as file:
    csvReader = csv.DictReader(file, delimiter=';')  # Указываем delimiter как ';'
    data = list(csvReader)  # Преобразуем данные в список словарей

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
