from options import database


def search():
    name = str(input('Введите Фамилию или Имя для поиска: '))
    flag = 0
    with open(database, 'r', encoding='utf-8') as data:
        lines = data.readlines()
        for line in lines:
            if name in line:
                print(line)
                flag = 1
            else:
                continue
    if flag == 0:
        print("По заданным параметрам данных не найдено.\n")