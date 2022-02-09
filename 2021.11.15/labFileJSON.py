import pandas as pd
import numpy as np
import chardet
import json

# Получаю dataFrame из json
def getDataFrame():
    with open('mosmetro.json', 'rb') as f:
        result = chardet.detect(f.read())
    station = pd.read_json('mosmetro.json', encoding=result['encoding'])
    station.head()
    return station

# Вывести в консоль список всех статусов станций (только уникальные значения)
def uniqueStatus():
    station = getDataFrame()
    statuses = station.to_dict('list')['Status'].copy()
    return set(statuses)

# Вывести в консоль список ТОП-10 районов с наибольшим количеством станций метрополитена в порядке возрастания
def topDistrict():
    station = getDataFrame()
    stations = station.to_dict('records').copy()
    dictDistricts = dict()

    for station in stations:
        if station['District'] in list(dictDistricts.keys()):
            dictDistricts[station['District']]+=1
        else:
            dictDistricts[station['District']] = 1

    sorted_dict = {}
    sorted_keys = sorted(dictDistricts, key=dictDistricts.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = dictDistricts[key]

    res = list()
    count = 0
    for key, value in sorted_dict.items():
        if count == 10:
            break
        res.append(key)
        count+=1
    return res

# Вывести в консоль список ТОП-5 веток метрополитена
# с наименьшим количеством действующих станций метро в порядке возрастания
def topLines():
    station = getDataFrame()
    stations = station.to_dict('records').copy()
    dictLines = dict()

    for station in stations:
        if station['Status'] == 'действует':
            if station['Line'] in list(dictLines.keys()):
                dictLines[station['Line']]+=1
            else:
                dictLines[station['Line']] = 1

    sorted_dict = {}
    sorted_keys = sorted(dictLines, key=dictLines.get)
    for key in sorted_keys:
        sorted_dict[key] = dictLines[key]
    res = list()
    count = 0
    for key, value in sorted_dict.items():
        if count == 5:
            break
        res.append(key)
        count+=1
    return res

# Создать json-файл где будут храниться только названия станций, линий и статусы станций
def createSimpleJSON():
    station = getDataFrame()
    stations = station.to_dict('records').copy()

    res = list()
    for elem in stations:
        temp = dict()
        temp['Station'] = elem['Station']
        temp['Line'] = elem['Line']
        temp['Status'] = elem['Status']
        res.append(temp)

    with open('simpleJson.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)

# Создать csv-файл с данными из json-файла в виде таблицы
def createSimpleCSV():
    station = getDataFrame()
    stations = station.to_dict('records').copy()
    station.to_csv('simpleCSV.csv', encoding='utf-8', sep = ",", index=False)

# Создать json-файл, где в виде двухуровневого списка хранить данные,
# основой список - ветки метро,
# а у каждой ветки будет вложенный список - станции с остальными параметрами, кроме названия ветки метро
def createSimpleJSON2():
    station = getDataFrame()
    stations = station.to_dict('records').copy()
    # print(stations)
    res = dict()
    for elem in stations:
        if elem['Line'] not in list(res.keys()):
            res[elem['Line']] = list()
        temp = dict()
        for key, value in elem.items():
            if key != 'Line':
                temp[key] = value
        res[elem['Line']].append(temp)

    with open('simpleJson2.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    createSimpleJSON2()
