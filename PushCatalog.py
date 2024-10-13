import csv
import json
import subprocess

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


# Отправка изменений в Git
#subprocess.run(['git', 'add', "."])
#subprocess.run(['git', 'commit', '-m', 'Updated JSON file'])
#subprocess.run(['git', 'push'])
