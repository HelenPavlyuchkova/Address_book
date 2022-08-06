import pandas as pd
import Import as ab_import
from options import database

#для импорта-экспорта нужен pandas: pip install pandas

#создает новые файлы
#ab_export.export_file("fio_export.csv", "csv")
#ab_export.export_file("fio_export.html", "html")
#ab_export.export_file("fio_export.json", "json")
#ab_export.export_file("fio_export.txt", "text")

#для Excel нужен модуль openpyxl: pip install openpyxl
#import openpyxl
#ab_export.export_file("fio_export.xlsx", "excel")

supported_export = ["csv", "excel", "html", "json", "text"]

# сохранение строки в файл
def write_file(target, str):
    with open(target, "w", encoding="utf-8") as f:
        return f.write(str)

def save(data):
    return save_data(database, "csv", data)

# запись данных DataFrame в файл
# mode: csv, excel, html, json, text
# нет обработки ошибок
def save_data(target, mode, data: pd.DataFrame):
    if mode == "csv":
        return data.to_csv(target, index=False, sep=";")
    if mode == "excel":
        return data.to_excel(target, index=False)
    if mode == "html":
        return write_file(target, data.to_html(index=False))
    if mode == "json":
        return write_file(target, data.to_json())
    if mode == "text":
        return write_file(target, data.to_string(index=False))

# экспорт текущей базы в файл
# зачитываем текущую базу
# экспортируем в другой формат
# mode: csv, excel, html, json, text
def export_file(target, mode):
    df = ab_import.load_data(database)
    return save_data(target, mode, df)

def export_data():
    mode = ""
    while mode not in supported_export:
        mode = input("Введите режим экспорта (" + ", ".join(supported_export) + "):")

    filename = input("Введите имя файла для экспорта (./Files/fio_export):")
    export_file(filename, mode)
    print(f"Данные были экспортированы в {filename}")
    return
