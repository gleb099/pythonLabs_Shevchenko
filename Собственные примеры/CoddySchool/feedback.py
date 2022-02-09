# -*- coding: utf8 -*-

import requests
import urllib.parse
import datetime
from pathlib import Path
import xlsxwriter
import re
import xlrd

workk = input("Что делаем?\n1. Работа с CRM 2. Работа со звоноботом\n")
if workk == "1":

    now = datetime.datetime.now()
    yearNow = now.year
    monthNow = now.month
    dayNow = now.day
    now = f"{yearNow}-{monthNow}-{dayNow}"

    # dateFromP = "2020-11-16"
    dateFromP = input("Введи начальную дату (YYYY-MM-DD)\n")
    dateFromPList = dateFromP.split("-")
    yearFrom = int(dateFromPList[0])
    monthFrom = int(dateFromPList[1])
    dayFrom = int(dateFromPList[2])

    # dateToP = "2021-03-01"
    dateToP = input("Введи конечную (YYYY-MM-DD)\n")
    dateToPList = dateToP.split("-")
    yearTo = int(dateToPList[0])
    monthTo = int(dateToPList[1])
    dayTo = int(dateToPList[2])

    dataUpload = int(
        input("Какую выгрузку делаем?(Введи цифру)\n1. Прошло два занятия \n2. Перед последним занятием\n"))
    branchs = ["Курская GlowByte", "Бутырская", "Владыкино Colvir Software Solution", "М.Видео-Эльдорадо",
               "Кузьминки(Жигулевская)", "Научный Парк МГУ", "На территории ученика", "Онлайн занятия",
               "Павелецкая SAP", "Пушкинская ФИНАМ", "Ростокино Электромузей", "Тульская Rambler Group",
               "Тульская Сбербанк Технологии", "Царицыно Загорье", "Чертановская QIWI", "ЭВОТОР (Парк Культуры)"]
    # branchs = ", ".join(branchs)

    both_key = ''  # key

    getStudents = "https://coddy.t8s.ru/Api/V2/GetStudents"
    getEdUnitStudents = "https://coddy.t8s.ru/Api/V2/GetEdUnitStudents"
    getEdUnits = "https://coddy.t8s.ru/Api/V2/GetEdUnits"

    # Выгрузка после первых двух занятий

    if dataUpload == 1:

        params = {'authkey': both_key, 'queryDays': 'true', 'levels': '-1'}
        params = urllib.parse.urlencode(params)
        # print("getEdUnits", params)
        print("Минутку, делаю выгрузку после первых двух занятий")

        r = requests.get(getEdUnits, params=params)
        dataUnits = r.json()['EdUnits']

        # for i in range(len(dataUnits)):
        # 	print(dataUnits[i])

        # data1 = dataUnits.copy()

        data1 = list()
        minDate = list()

        for i in range(len(dataUnits)):
            if dataUnits[i]["OfficeOrCompanyName"] in branchs:
                if 'Days' in list(dataUnits[i].keys()):
                    if len(dataUnits[i]['Days']) >= 3:
                        date1 = dataUnits[i]['Days'][0]['Date']
                        date1List = date1.split("-")
                        year1 = int(date1List[0])
                        month1 = int(date1List[1])
                        day1 = int(date1List[2])

                        date2 = dataUnits[i]['Days'][1]['Date']
                        date2List = date2.split("-")
                        year2 = int(date2List[0])
                        month2 = int(date2List[1])
                        day2 = int(date2List[2])

                        date3 = dataUnits[i]['Days'][2]['Date']
                        date3List = date3.split("-")
                        year3 = int(date3List[0])
                        month3 = int(date3List[1])
                        day3 = int(date3List[2])

                        if date2 >= dateFromP and date2 <= dateToP:  # проверяю, чтобы взять всех учеников которые занимаются
                            if date3 > dateToP:
                                # print(dataUnits[i])
                                # print()

                                # print()

                                data1.append(dataUnits[i])
                                minDate.append(dataUnits[i]['Days'][0]['Date'])


                    elif len(dataUnits[i]['Days']) == 2:
                        date1 = dataUnits[i]['Days'][0]['Date']
                        date1List = date1.split("-")
                        year1 = int(date1List[0])
                        month1 = int(date1List[1])
                        day1 = int(date1List[2])

                        date2 = dataUnits[i]['Days'][1]['Date']
                        date2List = date2.split("-")
                        year2 = int(date2List[0])
                        month2 = int(date2List[1])
                        day2 = int(date2List[2])

                        if date2 >= dateFromP and date2 <= dateToP:
                            # if year2 <= yearTo and month2 <= monthTo and day2 <= dayTo: #подумать на этот счет со временем
                            # print(dataUnits[i])
                            # print()
                            data1.append(dataUnits[i])
                            minDate.append(dataUnits[i]['Days'][0]['Date'])
        mind = min(minDate)

    # Выгрузка перед последним занятием

    elif dataUpload == 2:

        data1 = list()
        minDate = list()

        print(f'{len(branchs)} филиалов')

        for i in range(len(branchs)):

            params = {'authkey': both_key, 'queryDays': 'true', 'officeOrCompany': branchs[i], 'statuses': 'Working'}
            params = urllib.parse.urlencode(params)
            print("getEdUnits", params)
            print(f"Минутку, делаю выгрузку перед последним занятием для {i + 1} фила.")

            r = requests.get(getEdUnits, params=params)
            dataUnits = r.json()['EdUnits']

            for i in range(len(dataUnits)):
                if dataUnits[i]["OfficeOrCompanyName"] in branchs:

                    if 'Days' in list(dataUnits[i].keys()):
                        if len(dataUnits[i]['Days']) >= 2:
                            date1 = dataUnits[i]['Days'][-1]['Date']
                            date1List = date1.split("-")
                            year1 = int(date1List[0])
                            month1 = int(date1List[1])
                            day1 = int(date1List[2])

                            date2 = dataUnits[i]['Days'][-2]['Date']
                            date2List = date2.split("-")
                            year2 = int(date2List[0])
                            month2 = int(date2List[1])
                            day2 = int(date2List[2])

                            if date1 > dateToP:
                                if date2 >= dateFromP and date2 <= dateToP:  # подумать на этот счет со временем
                                    data1.append(dataUnits[i])
                                    minDate.append(dataUnits[i]['Days'][0]['Date'])
                                # print(dataUnits[i]["OfficeOrCompanyName"])
                                # print(data[i][''])

                    # elif len(dataUnits[i]['Days']) == 1:
                    # 	data1.append(dataUnits[i])
        mind = min(minDate)

    # for i in range(len(data1)):
    # 	print(data1[i])
    # 	print()

    # Чек посещения учеником занятий из data1

    data2 = list()

    params1 = {'authkey': both_key, 'queryDays': 'true', 'dateFrom': mind, 'dateTo': dateToP, 'take': 10000}
    params1 = urllib.parse.urlencode(params1)
    # print('getEdUnitStudents', params1)
    print("Проверяю посещения занятий учеником и добавляю инфу о преподавателях")

    r1 = requests.get(getEdUnitStudents, params=params1)
    dataUnitStudents = r1.json()['EdUnitStudents']

    for i in range(len(data1)):
        for j in range(len(dataUnitStudents)):
            if dataUnitStudents[j]["EdUnitOfficeOrCompanyName"] in branchs:
                if data1[i]["Id"] == dataUnitStudents[j]["EdUnitId"]:

                    if dataUpload == 1:

                        tempDates = list()
                        tempDates.append(data1[i]["Days"][0]["Date"])
                        tempDates.append(data1[i]["Days"][1]["Date"])

                        if (dataUnitStudents[j]["Days"][0]["Date"] in tempDates or dataUnitStudents[j]["Days"][1][
                            "Date"] in tempDates):

                            if len(dataUnitStudents[j]['Days']) >= 2:

                                if ((dataUnitStudents[j]["Days"][0]["Pass"] == False) or (
                                        dataUnitStudents[j]["Days"][1]["Pass"] == False)):

                                    # print(dataUnitStudents[j])
                                    # print()

                                    link = f"https://coddy.t8s.ru/Learner/{dataUnitStudents[j]['EdUnitType']}/{dataUnitStudents[j]['EdUnitId']}"
                                    tempDict = dict(StudentClientId=dataUnitStudents[j]["StudentClientId"],
                                                    StudentName=dataUnitStudents[j]["StudentName"],
                                                    EdUnitId=dataUnitStudents[j]["EdUnitId"], EdUnitLink=link)
                                    # добавление преподов(добавить позже диапазон дат у этих преподов)
                                    teachers = list()
                                    teacher = None
                                    for l in range(len(data1[i]['ScheduleItems'])):
                                        if 'Teacher' in list(data1[i]['ScheduleItems'][l]):
                                            if teacher not in teachers:
                                                teacher = data1[i]['ScheduleItems'][l]['Teacher']
                                                teachers.append(teacher)

                                    tempDict.setdefault(f'Teachers', teachers)
                                    # print(dataUnitStudents[j])

                                    data2.append(tempDict)

                    elif dataUpload == 2:

                        link = f"https://coddy.t8s.ru/Learner/{dataUnitStudents[j]['EdUnitType']}/{dataUnitStudents[j]['EdUnitId']}"
                        tempDict = dict(StudentClientId=dataUnitStudents[j]["StudentClientId"],
                                        StudentName=dataUnitStudents[j]["StudentName"],
                                        EdUnitId=dataUnitStudents[j]["EdUnitId"], EdUnitLink=link)
                        # добавление преподов(добавить позже диапазон дат у этих преподов)
                        teachers = list()
                        teacher = None
                        for l in range(len(data1[i]['ScheduleItems'])):
                            if "Teacher" in list(data1[i]['ScheduleItems'][l].keys()):
                                if teacher not in teachers:
                                    teacher = data1[i]['ScheduleItems'][l]['Teacher']
                                    teachers.append(teacher)
                                else:
                                    teachers.append(teacher)
                        tempDict.setdefault(f'Teachers', teachers)
                        # print(dataUnitStudents[j])

                        data2.append(tempDict)
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    for i in range(len(data2)):
        print(data2[i])
        print()

    # Организация выходных данных

    key = ''  # key
    params2 = {'authkey': key, 'statuses': 'Занимается', 'take': 10000}
    params2 = urllib.parse.urlencode(params2)
    print('getStudents', params2)
    r2 = requests.get(getStudents, params=params2)
    students = r2.json()['Students']
    print("Собираю инфу об агентах ученика и добавляю в выгрузку")

    agentsNone = list()
    # print(students)
    # for i in range(len(data2)):
    # 	print(data2[i])
    # 	print()

    for i in range(len(students)):
        for j in range(len(data2)):
            if students[i]['ClientId'] == data2[j]['StudentClientId']:
                # print(students[i])
                agentsFlag = True
                if 'Agents' not in list(students[i].keys()):  # ребята без агентов
                    agentsNone.append(students[i])
                    agentsFlag = False

                if 'FirstName' in list(students[i].keys()):
                    data2[j].setdefault('FirstName', students[i]['FirstName'])
                else:
                    data2[j].setdefault('FirstName')
                if 'LastName' in list(students[i].keys()):
                    data2[j].setdefault('LastName', students[i]['LastName'])
                else:
                    data2[j].setdefault('LastName')

                if agentsFlag == True:
                    ph = -100
                    for k in range(len(students[i]['Agents'])):

                        if 'AgentMobile' in list(data2[j].keys()):
                            break
                        if 'Mobile' in list(students[i]['Agents'][k].keys()):
                            data2[j].setdefault('AgentMobile', students[i]['Agents'][k]['Mobile'])
                            ph = k
                        elif 'Phone' in list(students[i]['Agents'][k].keys()):
                            data2[j].setdefault('AgentMobile', students[i]['Agents'][k]['Phone'])
                            ph = k

                    if 'AgentMobile' not in list(data2[j].keys()):
                        if ('Mobile' in list(students[i].keys())):
                            data2[j].setdefault('AgentMobile', students[i]['Mobile'])
                        elif ('Phone' in list(students[i].keys())):
                            data2[j].setdefault('AgentMobile', students[i]['Phone'])
                        else:
                            data2[j].setdefault('AgentMobile')

                    if ph != -100:
                        if 'FirstName' in list(students[i]['Agents'][ph].keys()):
                            data2[j].setdefault('AgentFirstName', students[i]['Agents'][ph]['FirstName'])
                        else:
                            data2[j].setdefault('AgentFirstName')
                        if 'LastName' in list(students[i]['Agents'][ph].keys()):
                            data2[j].setdefault('AgentLastName', students[i]['Agents'][ph]['LastName'])
                        else:
                            data2[j].setdefault('AgentLastName')
                    else:
                        if 'FirstName' in list(students[i]['Agents'][0].keys()):
                            data2[j].setdefault('AgentFirstName', students[i]['Agents'][0]['FirstName'])
                        else:
                            data2[j].setdefault('AgentFirstName')
                        if 'LastName' in list(students[i]['Agents'][0].keys()):
                            data2[j].setdefault('AgentLastName', students[i]['Agents'][0]['LastName'])
                        else:
                            data2[j].setdefault('AgentLastName')
                else:
                    data2[j].setdefault('AgentFirstName')
                    data2[j].setdefault('AgentLastName')
                    if ('Mobile' in list(students[i].keys())):
                        data2[j].setdefault('AgentMobile', students[i]['Mobile'])
                    elif ('Phone' in list(students[i].keys())):
                        data2[j].setdefault('AgentMobile', students[i]['Phone'])
                    else:
                        data2[j].setdefault('AgentMobile')

    print("=========================AgentMobile============================================")
    print("=========================AgentMobile=============================================")
    print("=================================AgentMobile==========================================")
    print("===========================AgentMobile==============================================")
    print("===============================AgentMobile=========================================")
    print("============================AgentMobile==============================================")

    for k in range(len(data2)):
        if 'AgentMobile' not in list(data2[k].keys()):

            key = ''  # key
            params2 = {'authkey': key, 'clientId': data2[k]['StudentClientId']}
            params2 = urllib.parse.urlencode(params2)
            print('getStudents', params2)
            r2 = requests.get(getStudents, params=params2)
            students = r2.json()['Students']
            print("Собираю инфу о конкретных учениках из-за этого вонючего обновления")

            for i in range(len(students)):
                for j in range(len(data2)):
                    if students[i]['ClientId'] == data2[j]['StudentClientId']:
                        # print(students[i])
                        agentsFlag = True
                        if 'Agents' not in list(students[i].keys()):  # ребята без агентов
                            agentsNone.append(students[i])
                            agentsFlag = False

                        if 'FirstName' in list(students[i].keys()):
                            data2[j].setdefault('FirstName', students[i]['FirstName'])
                        else:
                            data2[j].setdefault('FirstName')
                        if 'LastName' in list(students[i].keys()):
                            data2[j].setdefault('LastName', students[i]['LastName'])
                        else:
                            data2[j].setdefault('LastName')

                        if agentsFlag == True:
                            ph = -100
                            for k in range(len(students[i]['Agents'])):

                                if 'AgentMobile' in list(data2[j].keys()):
                                    break
                                if 'Mobile' in list(students[i]['Agents'][k].keys()):
                                    data2[j].setdefault('AgentMobile', students[i]['Agents'][k]['Mobile'])
                                    ph = k
                                elif 'Phone' in list(students[i]['Agents'][k].keys()):
                                    data2[j].setdefault('AgentMobile', students[i]['Agents'][k]['Phone'])
                                    ph = k

                            if 'AgentMobile' not in list(data2[j].keys()):
                                if ('Mobile' in list(students[i].keys())):
                                    data2[j].setdefault('AgentMobile', students[i]['Mobile'])
                                elif ('Phone' in list(students[i].keys())):
                                    data2[j].setdefault('AgentMobile', students[i]['Phone'])
                                else:
                                    data2[j].setdefault('AgentMobile')

                            if ph != -100:
                                if 'FirstName' in list(students[i]['Agents'][ph].keys()):
                                    data2[j].setdefault('AgentFirstName', students[i]['Agents'][ph]['FirstName'])
                                else:
                                    data2[j].setdefault('AgentFirstName')
                                if 'LastName' in list(students[i]['Agents'][ph].keys()):
                                    data2[j].setdefault('AgentLastName', students[i]['Agents'][ph]['LastName'])
                                else:
                                    data2[j].setdefault('AgentLastName')
                            else:
                                if 'FirstName' in list(students[i]['Agents'][0].keys()):
                                    data2[j].setdefault('AgentFirstName', students[i]['Agents'][0]['FirstName'])
                                else:
                                    data2[j].setdefault('AgentFirstName')
                                if 'LastName' in list(students[i]['Agents'][0].keys()):
                                    data2[j].setdefault('AgentLastName', students[i]['Agents'][0]['LastName'])
                                else:
                                    data2[j].setdefault('AgentLastName')
                        else:
                            data2[j].setdefault('AgentFirstName')
                            data2[j].setdefault('AgentLastName')
                            if ('Mobile' in list(students[i].keys())):
                                data2[j].setdefault('AgentMobile', students[i]['Mobile'])
                            elif ('Phone' in list(students[i].keys())):
                                data2[j].setdefault('AgentMobile', students[i]['Phone'])
                            else:
                                data2[j].setdefault('AgentMobile')

            print(data2[i])
            print()

    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")
    print("====================================================================================")

    for i in range(len(agentsNone)):
        print(agentsNone[i])
        print()

    # Обработка номера телефона

    print("Привожу номера телефонов в единый вид")

    foreign = list()
    data_preFin = list()

    for i in range(len(data2)):
        # print(data2[i])
        if 'AgentMobile' in list(data2[i].keys()):
            # print(data2[i])
            number = data2[i]['AgentMobile']
            if number == None:
                foreign.append(data2[i])
            else:
                number = list(number)
                temp = list()
                for j in range(len(number)):
                    if number[j].isdigit():
                        temp.append(number[j])
                if temp[0] == "7":
                    temp.insert(0, "+")
                number1 = ''.join(temp)
                # print(number1)
                data2[i]['AgentMobile'] = number1

                # чек на иностранный элемент

                pattern = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7}$')
                m = pattern.match(number1)
                if not m:
                    foreign.append(data2[i])
                else:
                    data_preFin.append(data2[i])
        else:
            print("=========================AgentNONE=============================================")
            print("============================AgentNONE=============================================")
            print("=================================AgentNONE===========================================")
            print("============================AgentNONE================================================")
            print("===============================AgentNONE========================================")
            print("===============================AgentNONE=========================================")
            print(data2[i])

    # for i in range(len(foreign)):
    # 	print(foreign[i])
    # 	print()

    # for i in range(len(data2)):
    # 	print(data2[i])
    # 	print()

    if dataUpload == 1:
        # добавление в Excel c русскими номерами level -1
        finalData = data_preFin.copy()

        workbook = xlsxwriter.Workbook(f'{dateFromP}-{dateToP}_rus(lev_-1).xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write("A1", "Номер телефона", bold)
        worksheet.write("B1", "ФИО ученика", bold)
        worksheet.write("C1", "ФИО родителя", bold)
        worksheet.write("D1", "Преподаватель", bold)
        worksheet.write("E1", "Ссылка на учебную единицу", bold)

        for i in range(len(finalData)):
            worksheet.write(f'A{i + 2}', finalData[i]['AgentMobile'])
            worksheet.write(f'B{i + 2}', finalData[i]['StudentName'])
            if finalData[i]['AgentFirstName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentLastName'])
            elif finalData[i]['AgentLastName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentFirstName'])
            else:
                fio = f"{finalData[i]['AgentFirstName']} {finalData[i]['AgentLastName']}"
                worksheet.write(f'C{i + 2}', fio)
            if "Teachers" not in list(finalData[i].keys()):
                worksheet.write(f'D{i + 2}', 'Нет препода')
            else:
                if len(finalData[i]['Teachers']) >= 1:
                    worksheet.write(f'D{i + 2}', finalData[i]['Teachers'][-1])
                else:
                    worksheet.write(f'D{i + 2}', 'Нет препода')
            worksheet.write(f'E{i + 2}', finalData[i]['EdUnitLink'])

        workbook.close()

        # добавление в Excel c иностранными номерами level -1

        finalData = foreign.copy()

        workbook = xlsxwriter.Workbook(f'{dateFromP}-{dateToP}_foreign(lev_-1).xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write("A1", "Номер телефона", bold)
        worksheet.write("B1", "ФИО ученика", bold)
        worksheet.write("C1", "ФИО родителя", bold)
        worksheet.write("D1", "Преподаватель", bold)
        worksheet.write("E1", "Ссылка на учебную единицу", bold)

        for i in range(len(finalData)):
            worksheet.write(f'A{i + 2}', finalData[i]['AgentMobile'])
            worksheet.write(f'B{i + 2}', finalData[i]['StudentName'])
            if finalData[i]['AgentFirstName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentLastName'])
            elif finalData[i]['AgentLastName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentFirstName'])
            else:
                fio = f"{finalData[i]['AgentFirstName']} {finalData[i]['AgentLastName']}"
                worksheet.write(f'C{i + 2}', fio)
            worksheet.write(f'D{i + 2}', finalData[i]['Teachers'][-1])
            worksheet.write(f'E{i + 2}', finalData[i]['EdUnitLink'])

        workbook.close()

    elif dataUpload == 2:
        # добавление в Excel c русскими номерами level ALL
        finalData = data_preFin.copy()

        workbook = xlsxwriter.Workbook(f'{dateFromP}-{dateToP}_rus(lev_ALL).xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write("A1", "Номер телефона", bold)
        worksheet.write("B1", "ФИО ученика", bold)
        worksheet.write("C1", "ФИО родителя", bold)
        worksheet.write("D1", "Преподаватель", bold)
        worksheet.write("E1", "Ссылка на учебную единицу", bold)

        for i in range(len(finalData)):
            worksheet.write(f'A{i + 2}', finalData[i]['AgentMobile'])
            worksheet.write(f'B{i + 2}', finalData[i]['StudentName'])
            if finalData[i]['AgentFirstName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentLastName'])
            elif finalData[i]['AgentLastName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentFirstName'])
            else:
                fio = f"{finalData[i]['AgentFirstName']} {finalData[i]['AgentLastName']}"
                worksheet.write(f'C{i + 2}', fio)
            worksheet.write(f'D{i + 2}', finalData[i]['Teachers'][-1])
            worksheet.write(f'E{i + 2}', finalData[i]['EdUnitLink'])

        workbook.close()

        # добавление в Excel c иностранными номерами level ALL

        finalData = foreign.copy()

        workbook = xlsxwriter.Workbook(f'{dateFromP}-{dateToP}_foreign(lev_ALL).xlsx')
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})
        worksheet.write("A1", "Номер телефона", bold)
        worksheet.write("B1", "ФИО ученика", bold)
        worksheet.write("C1", "ФИО родителя", bold)
        worksheet.write("D1", "Преподаватель", bold)
        worksheet.write("E1", "Ссылка на учебную единицу", bold)

        for i in range(len(finalData)):
            worksheet.write(f'A{i + 2}', finalData[i]['AgentMobile'])
            worksheet.write(f'B{i + 2}', finalData[i]['StudentName'])
            if finalData[i]['AgentFirstName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentLastName'])
            elif finalData[i]['AgentLastName'] == None:
                worksheet.write(f'C{i + 2}', finalData[i]['AgentFirstName'])
            else:
                fio = f"{finalData[i]['AgentFirstName']} {finalData[i]['AgentLastName']}"
                worksheet.write(f'C{i + 2}', fio)
            worksheet.write(f'D{i + 2}', finalData[i]['Teachers'][-1])
            worksheet.write(f'E{i + 2}', finalData[i]['EdUnitLink'])

        workbook.close()

    print("Все готово, готовые таблички лежат в одной папке с программой")

else:

    rb = xlrd.open_workbook('Book1.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    val = sheet.row_values(0)[0]

    vals = list()
    for i in range(sheet.nrows):
        vals.append(sheet.row_values(i))

    nones = list()
    for i in range(len(vals)):
        if vals[i][1] == "":
            nones.append(vals[i][0])

    workbook = xlsxwriter.Workbook(f'after_zvonobot.xlsx')
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})
    worksheet.write("A1", "Номер телефона", bold)

    for i in range(len(nones)):
        worksheet.write(f'A{i + 2}', nones[i])

    workbook.close()
