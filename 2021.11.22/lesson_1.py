# Красивый вывод таблицы в терминал
from prettytable import PrettyTable
from prettytable import from_csv
import prettytable

# Простое добавление данных в таблицу

# Построчное
def addData1():
    ta = PrettyTable()
    ta.field_names = ["Surname", "Name", "Age", "Salary"] # Заголовок таблицы
    ta.add_row(["Ivanov", "Ivan", 19, 30000])
    ta.add_row(["Ivanov1", "Ivan1", 19, 30000])
    ta.add_row(["Ivanov2", "Ivan2", 19, 30000])
    ta.add_row(["Ivanov3", "Ivan3", 19, 30000])
    print(ta)

# Сразу списком
def addData2():
    ta = PrettyTable()
    ta.field_names = ["Surname", "Name", "Age", "Salary"] # Заголовок таблицы
    ta.add_rows(
        [
            ["Ivanov", "Ivan", 19, 30000],
            ["Ivanov1", "Ivan1", 28, 40000],
            ["Ivanov2", "Ivan2", 10, 32000],
            ["Ivanov3", "Ivan3", 25, 10000],
        ]
    )
    return ta

# Копия таблицы
def copyTable():
    ta = addData2()
    ta2 = ta
    print(ta2)

    ta3 = ta[:-2]
    print(ta3)

# Выравнивание данных в таблице
def alignData():
    ta = addData2()
    ta.align = 'l' # варианты  (l, r, c)
    ta.align['Surname'] = 'l' # отдельно на каждый столбец по ключу
    ta.align['Name'] = 'r'
    print(ta)

# Сортировка данных в таблице
def sortData():
    ta = addData2()
    print(ta.get_string(sortby="Age", reversesort = True))

# Изменить отображение столбцов и количество строк
def reView():
    ta = addData2()
    print(ta.get_string(start=1, end=3)) # по количеству строк
    print(ta.get_string(fields=["Name", "Age"])) # по столбцам

# Изменить рамку
def newBorder():
    ta = addData2()
    ta.set_style(prettytable.MSWORD_FRIENDLY)
    ta.set_style(prettytable.DOUBLE_BORDER)
    ta.set_style(prettytable.DEFAULT)
    print(ta)

# Изменить рамку
def newBorder2():
    ta = addData2()
    ta.border = False
    print(ta.get_string(border = True))
    print(ta)

# Экспортирование таблицы в другой формат
def exportToAnyFormat():
    ta = addData2()
    # print(ta.get_csv_string())
    # print(ta.get_json_string(ensure_ascii = False))
    print(ta.get_html_string(attributes={"id":"my_table", "class": "super_table"}))

# Импортирование данных из CSV
def importFromCSV():
    ta = addData2()

    with open("cities.csv") as f: # без энкодинга все с кайфом работает
        ta = from_csv(f)
    print(ta[0:7])

if __name__ == "__main__":
    importFromCSV()