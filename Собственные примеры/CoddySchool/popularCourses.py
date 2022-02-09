# -*- coding: utf8 -*-

import requests
import urllib.parse
import datetime
from pathlib import Path
import xlsxwriter
import re
import xlrd

now = datetime.datetime.now()
yearNow = now.year
monthNow = now.month
dayNow = now.day
now = f"{yearNow}-{monthNow}-{dayNow}"

dateFromP = "2016-01-01"
# dateFromP = input("Введи начальную дату (YYYY-MM-DD)\n")
dateFromPList = dateFromP.split("-")
yearFrom = int(dateFromPList[0])
monthFrom = int(dateFromPList[1])
dayFrom = int(dateFromPList[2])

dateToP = "2016-02-01"
# dateToP = input("Введи конечную (YYYY-MM-DD)\n")
dateToPList = dateToP.split("-")
yearTo = int(dateToPList[0])
monthTo = int(dateToPList[1])
dayTo = int(dateToPList[2])

branchs = ["Курская GlowByte", "Бутырская", "Владыкино Colvir Software Solution", "М.Видео-Эльдорадо",
           "Кузьминки(Жигулевская)", "Научный Парк МГУ", "На территории ученика", "Онлайн занятия", "Павелецкая SAP",
           "Пушкинская ФИНАМ", "Ростокино Электромузей", "Тульская Rambler Group", "Тульская Сбербанк Технологии",
           "Царицыно Загорье", "Чертановская QIWI", "ЭВОТОР (Парк Культуры)"]
# branchs = ", ".join(branchs)

both_key = ''  # key

getStudents = "https://coddy.t8s.ru/Api/V2/GetStudents"
getEdUnitStudents = "https://coddy.t8s.ru/Api/V2/GetEdUnitStudents"
getEdUnits = "https://coddy.t8s.ru/Api/V2/GetEdUnits"

dateFromP = "2016-01-01"
dateToP = "2016-02-01"

year = ['2016', '2017', '2018', '2019', '2020']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

fyFrom = 0
fmFrom = 0

fyTo = 0
fmTo = 1

km = 0

dis = ['Создание сайтов HTML, CSS', 'Дизайн-мышление', 'Мобильные приложения', 'Муз. программирование (больше нет)',
       '2D-анимация (больше нет)', 'Создание игр в Scratch', 'Программирование для самых маленьких',
       'Создание сайтов на WordPress', 'Стартапы', 'Программирование игр на Python', 'Игровое 3D-моделирование',
       'Графический дизайн Photoshop', 'Английский в программировании', 'Графический дизайн и брендинг (больше нет)',
       'Гарвардский курс', 'Программирование на JavaScript', 'Моушен дизайн', 'Кукарача Windows',
       'Компьютерная грамотность', 'Моб. игры на Stencyl (больше нет)', 'Видеоблогинг', 'Мнемоника (больше нет)',
       'Web-мастеринг', 'Startup English', 'Apple Swift', 'Дизайн мобильных приложений', 'PHP и MySQL',
       'Создание игр в Construct2', 'Illustrator для начинающих', 'Minacraft в Scratch',
       'Разработка сценария игр (сейчас нет)', 'Финансовая грамотность', 'Боты на Python', 'Игры на С++',
       'Ораторское мастерство', 'Этичный хакер', 'Интернет-предпринимательство', 'Фузионизм', 'Экскурсии',
       'Создание игр в Snap', 'Unity 3D', 'Веб-приложения', 'Стратегия Го', 'CodeCombat', 'Python и машинное обучение',
       'Программирование Java', 'Программирование для самых маленьких в  Tynker', 'Игры на C#',
       'Презентация PowerPoint', 'English&Python', 'Блоггинг и новые медиа', 'Дизайн сайтов',
       'Программирование Minecraft', 'Объемно-пространственное мышление (больше нет)', 'Дизайн социальных сетей',
       'Видеомонтаж', 'Рисование в стиле аниме', 'Веб-дизайн с нуля', 'Unreal Engine 4', 'Технология блокчейн',
       'Программирование Kodu Game Lab', 'Интересный китайский', '3D игры в Scratch', 'Программирование роботов',
       'Подготовка к ОГЭ по математике', 'Актерское мастерство', 'Minecraft на Python', 'Мастер коммуникации',
       'Я выбираю профессию', 'CryEngine5', 'Город будущего', 'Скорочтение и мнемоника', 'Кибер-безопасность',
       'Программирование на Lua в Minecraft', 'Трехмерное моделирование в 3ds max', 'Программирование в Roblox',
       'Дополненная реальность', 'Киберспорт', 'Олимпиадное программирование', 'Стэнфордский курс', 'Каллиграфия',
       'Pasсal', 'Русский язык и культура речи', 'Операторское мастерство', 'Marvel в Photoshop',
       'Problem solving-развитие системного мышления.', 'Создание мини-мультфильмов',
       'Программирование чат-ботов и игр на Python (при партнерстве с ВМК МГУ имени М.В. Ломоносова)',
       'Создание мобильных приложений на Android', 'Сайты на Python', 'Создание комиксов Манга', 'Английский',
       'Цифровой рисунок', 'Minecraft введение в искусственный интеллект',
       'Веб-приложения на Python при партнерстве с ВМК МГУ', 'Рисование на графических планшетах', '3D анимация Maya',
       'Разработка приложения для Google Ассистента при поддержке специалистов из Google',
       'Основы программирования и алгоритмики', 'Программирование на Python', 'Скетчинг', 'Подготовка к школе',
       'Группа кратковременного пребывания', 'Приложения на Unity', 'Математика', 'Физика', 'Робототехника',
       'Подготовка к ЕГЭ по информатике']

data_dis = list()

for i in range(len(dis)):
    temp = dict(name_dis=dis[i], count_mod=0)
    data_dis.append(temp)

while True:

    params1 = {'authkey': both_key, 'dateFrom': dateFromP, 'dateTo': dateToP}
    # params1 = {'authkey': both_key}

    params1 = urllib.parse.urlencode(params1)
    print('getEdUnitStudents', params1)
    print()

    r1 = requests.get(getEdUnitStudents, params=params1)
    data = r1.json()['EdUnitStudents']

    km += len(data)
    print(km)
    print(f'Количество модулей с {dateFromP} до {dateToP} - {len(data)}')

    dateFromPList = dateFromP.split("-")
    dateToPList = dateToP.split("-")

    fmFrom += 1
    if fmFrom >= len(month):
        fmFrom = 0
        fyFrom += 1

    fmTo += 1
    if fmTo >= len(month):
        fmTo = 0
        fyTo += 1

    dateFromPList[0] = year[fyFrom]
    dateFromPList[1] = month[fmFrom]

    dateToPList[0] = year[fyTo]
    dateToPList[1] = month[fmTo]

    dateToP = '-'.join(dateToPList)
    dateFromP = '-'.join(dateFromPList)

    print(dateFromP, dateToP)

    # получаем все дисциплины
    for i in range(len(data)):
        if 'EdUnitDiscipline' in list(data[i].keys()):
            if data[i]['EdUnitDiscipline'] not in dis:
                dis.append(data[i]['EdUnitDiscipline'])

    # получаем количество каждой дисциплины
    for i in range(len(data)):
        for j in range(len(data_dis)):
            if data[i]['EdUnitDiscipline'] == data_dis[j]['name_dis']:
                data_dis[j]['count_mod'] += 1

    if dateToP == "2020-10-01":
        break

print('Всего модулей -', km)

# for i in range(len(data)):
# 	print(data[i])
# 	print()


# Поключаемся к студентам, чтобы получить общее количество клиентов

key = ''  # key
params2 = {'authkey': key}
params2 = urllib.parse.urlencode(params2)

print('getStudents', params2)
r2 = requests.get(getStudents, params=params2)
students = r2.json()['Students']

n = len(students)
print(f'Всего уникальных клиентов - {n}')

# Вычисление конечного результата
result = km / n
print("LTV =", result)

# Работа с курсами
# print(dis)

count_dis = 0

for i in range(len(data_dis)):
    # print(data_dis[i])
    count_dis += data_dis[i]['count_mod']

print()
print('Сумма по итогу =', count_dis)
print('Всего модулей', km)

data_dis2 = data_dis.copy()

for i in range(len(data_dis2)):
    per = (data_dis2[i]['count_mod'] * 100) / count_dis
    data_dis2[i]['persent'] = per

both_per = 0

for i in range(len(data_dis2)):
    print(data_dis2[i])
    both_per += data_dis2[i]['persent']

print('Общий процент с погрешностью', both_per)

# Запихиваем все это в табличку экселевскую

finalData = data_dis2.copy()

workbook = xlsxwriter.Workbook(f'Popular_courses.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
worksheet.write("A1", "Курс", bold)
worksheet.write("B1", "В процентах", bold)

for i in range(len(finalData)):
    worksheet.write(f'A{i + 2}', finalData[i]['name_dis'])
    worksheet.write(f'B{i + 2}', finalData[i]['persent'])

workbook.close()

print("Табличка со статой в папке с проектом")