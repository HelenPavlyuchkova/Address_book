import os
import pandas as pd
from options import database
import Export as ab_export

#добавляет в текущий файл новые данные
#ab_import.import_file("fio_import.csv")

# загрузка данных
# читаем CSV файл, возвращаем DataFrame
# нет обработки ошибок
def load_data(filename):
    return pd.read_csv(filename, sep=";")

def load():
    return load_data(database)

def import_data(data):
    db = load_data(database)
    max_id = db["id"].max() + 1
    data['id'] = range(max_id, max_id+len(data))
    result = pd.concat([db, data])
    ab_export.save_data(database, "csv", result)
    return data

# импорт
# 1) зачитываем текущую базу
# 2) добавляем новые данные (вопрос: нужна проверка на дубликаты?)
# 3) при добавлении создаем новый уникальный id
# 4) сохраняем в текущую базу 
def import_file(filename):
    return import_data(load_data(filename))

def importf():
    filename = ""
    while len(filename) == 0:
        filename = input("Введите имя CSV Файла для импорта(./Files/fio_import.csv):")
        if not os.path.exists(filename):
            print(f"Файл {filename} не существует!")
            filename = ""
        else:
            df = import_file(filename)
            print("%d учеников импортировано" % len(df))

    return