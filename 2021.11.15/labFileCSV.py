import pandas as pd
import numpy as np
import chardet

def getDataFrame():
    with open('cities_russia.csv', 'rb') as f:
        result = chardet.detect(f.read())

    dataFrame = pd.read_csv('cities_russia.csv', delimiter=';', encoding=result['encoding'])
    dataFrame = dataFrame.to_dict('list')
    return dataFrame

#Вывод всех городов, в названии которых есть буквы "ы"
def cities():
    cities = getDataFrame()['Город'].copy()
    for city in cities:
        for i in range(len(city)):
            if city[i] == 'ы':
                print(city)

#Вывод в консоль городов, название которых содержит до
#4х букв включительно и отсортированные в обратном алфавитном порядке
def cities4():
    cities = getDataFrame()['Город'].copy()
    res = list()
    for city in cities:
        cityMass = list(city)
        if len(cityMass) <= 4:
            sortCity = cityMass.sort(reverse=True)
            # print(f"{''.join(cityMass)} - {''.join(city)}")
            if ''.join(cityMass) == ''.join(city):
                res.append(city)
    return res

#Вывод в консоль городов, название которых содержит до
#4х букв включительно и отсортированные в обратном алфавитном порядке
def cities4_1():
    cities = getDataFrame()['Город'].copy()
    resList = list()
    for city in cities:
        if len(city) <= 4:
            resList.append(city)
    resList.sort(reverse=True)
    return resList

# Вывести в консоль все буквы алфавита и рядом количество городов, начинающихся на каждую букву
def alph():
    cities = getDataFrame()['Город'].copy()
    a = ord('а')
    strAlphabet = list(''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]))

    res = list()
    resDict = dict()
    for el in cities:
        if el[0].lower() in list(resDict.keys()):
            resDict[el[0].lower()].append(el)
        else:
            resDict[el[0].lower()] = []
            resDict[el[0].lower()].append(el[0])

    for letter in strAlphabet:
        if letter in list(resDict.keys()):
            res.append((letter, len(resDict[letter])))
    return res

# Вывести в консоль ТОП-10 городов с самыми длинными названиями
def top10_1():
    cities = getDataFrame()['Город'].copy()
    cities2 = cities.copy()
    cities2.sort(key = lambda s: len(s), reverse = True)

    res = list()
    for i in range(10):
        res.append(cities2[i])
    return res

# Вывести в консоль список ТОП-10 городов, в названии которых больше всего согласных букв
def top10_2():
    def count_vowels(word, vowels=st1):
        return sum(1 for char in word if char in vowels)
    st = 'цкнгшщзхфвпрлджчсмт'
    st1 = st + st.upper()

    cities = getDataFrame()['Город'].copy()
    cities2 = cities.copy()
    cities2.sort(key = lambda s: count_vowels(s), reverse = True)

    res = list()
    for i in range(10):
        res.append((cities2[i], len(cities2[i])))
    return res

# Вывести в консоль список ТОП-10 букв, которые используются чаще всего в названии городов
def top10_3():
    cities = getDataFrame()['Город'].copy()
    a = ord('а')
    strAlphabet = list(''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]))
    res = list()

    resDict = dict()
    for el in cities:
        if el[0].lower() in list(resDict.keys()):
            resDict[el[0].lower()] += 1
        else:
            resDict[el[0].lower()] = 1

    sorted_dict = {}
    sorted_keys = sorted(resDict, key=resDict.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = resDict[key]
    count = 0
    for key, value in sorted_dict.items():
        if count == 10:
            break
        res.append(key)
        count+=1

    return res

if __name__ == "__main__":
    print(alph())

