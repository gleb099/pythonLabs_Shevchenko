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

dateFromP = "2020-01-01"
# dateFromP = input("Введи начальную дату (YYYY-MM-DD)\n")
dateFromPList = dateFromP.split("-")
yearFrom = int(dateFromPList[0])
monthFrom = int(dateFromPList[1])
dayFrom = int(dateFromPList[2])

dateToP = "2020-02-01"
# dateToP = input("Введи конечную (YYYY-MM-DD)\n")
dateToPList = dateToP.split("-")
yearTo = int(dateToPList[0])
monthTo = int(dateToPList[1])
dayTo = int(dateToPList[2])

branchs = ["Курская GlowByte", "Бутырская", "Владыкино Colvir Software Solution", "М.Видео-Эльдорадо", "Кузьминки(Жигулевская)", "Научный Парк МГУ", "На территории ученика", "Онлайн занятия", "Павелецкая SAP", "Пушкинская ФИНАМ", "Ростокино Электромузей", "Тульская Rambler Group", "Тульская Сбербанк Технологии", "Царицыно Загорье", "Чертановская QIWI", "ЭВОТОР (Парк Культуры)"]
# branchs = ", ".join(branchs)

both_key = '' #key

getStudents = "https://coddy.t8s.ru/Api/V2/GetStudents"
getEdUnitStudents = "https://coddy.t8s.ru/Api/V2/GetEdUnitStudents"
getEdUnits = "https://coddy.t8s.ru/Api/V2/GetEdUnits"
getTeachers = "https://coddy.t8s.ru/Api/V2/GetTeachers"

dateFromP = "2016-01-01"
dateToP = "2016-02-01"

mind = "2021-01-01"

year = ['2016', '2017', '2018', '2019', '2020', '2021']
# month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# year = ['2020', '2021']
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

fyFrom = 0
fmFrom = 0

fyTo = 0
fmTo = 1

km = 0

count_st = 0
count_mod = 0

teach_units = list()

data2 = list() #list with all study units students


#Все EdUnits

while True:

	print(dateFromP, dateToP)

	params1 = {'authkey': both_key, 'queryDays': 'true', 'dateFrom': dateFromP, 'dateTo': dateToP}
	params1 = urllib.parse.urlencode(params1)
	print('getEdUnitStudents', params1)
	# print("Просто чек")

	r1 = requests.get(getEdUnitStudents, params=params1)
	data = r1.json()['EdUnitStudents']

	for i in range(len(data)):
		data2.append(data[i])


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

	if dateToP == "2021-01-01":
		break

#в data2 лежит весь массив EdUnitStudents с 2016

# собираем всех преподов
params = {'authkey': both_key}
params = urllib.parse.urlencode(params)

r = requests.get(getTeachers, params=params)
data = r.json()['Teachers']

dataTeachers = list()
noStatus = list()

for i in range(len(data)):
	if ('Status' not in list(data[i].keys())) or ('Fired' not in list(data[i].keys())):
		noStatus.append(data[i])
		continue
	if data[i]['Status'] == 'Уволен' or data[i]['Fired'] == True:
		continue

	teachDict = dict()
	name = data[i]['LastName']
	surname = data[i]['FirstName']
	name = name + ' ' + surname
	date = data[i]['Created'].split('-')
	date = date[0] + '-' + date[1] + '-' + '01'

	teachDict.setdefault('date', date)
	teachDict.setdefault('name', name)
	teachDict.setdefault('id', data[i]['Id'])

	dataTeachers.append(teachDict)

#в dataTeachers все преподы


ltv_teach_list = list()

for t in range(len(dataTeachers)):
	teachEdId = list()
	# print(dataTeachers[t])
	# print()

	params = {'authkey': both_key, 'queryDays': 'true', 'teacherId': dataTeachers[t]['id']}
	params = urllib.parse.urlencode(params)

	r = requests.get(getEdUnits, params=params)
	data = r.json()['EdUnits']

	for i in range(len(data)):
		if data[i]['StudentsCount'] != 0:
			# te = dict(pre = dataTeachers[t], ed = data[i])
			teachEdId.append(data[i])

	#Обрабатываю каждого препода и считаю его ltv

	# for i in range(len(teachEdId)):
	# 	print(teachEdId[i])
	# 	print()

	# a = int(input("Stop"))

	types = ['Group', 'MiniGroup', 'Individual']
	studentId = list()
	edId = list()

	count_mod = 0
	count_st = 0

	temp = list()

	for i in range(len(teachEdId)):
		for j in range(len(data2)):
			if data2[j]['EdUnitId'] == teachEdId[i]['Id']:
				temp.append(data2[j])
				count_mod += 1
				# print("-------------------------------------------")
				# print(data2[j])

				if data2[j]['StudentClientId'] not in studentId:
					count_st += 1
					studentId.append(data2[j]['StudentClientId'])

	print('count_mod', count_mod)
	print('count_st', count_st)

	if count_mod == 0 or count_st == 0:
		noStatus.append(dataTeachers[t])
		continue

	ltv_counch = count_mod / count_st
	print('LTV_counch', ltv_counch)

	print('-----------------Статистика по занятиям-----------------')

	stMod = 0
	stModCheck = 0

	students = list()

	for j in range(len(studentId)):

		stMod = 0

		for i in range(len(temp)):
			if studentId[j] == temp[i]['StudentClientId']:
				stMod += 1
				namest = temp[i]['StudentName']
				dis = temp[i]['EdUnitDiscipline']
				stModCheck += 1

		temp_d = dict(name = namest, id = temp[i]['StudentClientId'], count_mod = stMod, dis = dis)
		students.append(temp_d)
		# print(namest, stMod)


	print('LTV_couch_check', stModCheck / len(students))


	dis_p = list()
	for di in range(len(students)):
		if students[di]['dis'] not in dis_p:
			dis_p.append(students[di]['dis'])

	#считаю количество модулей по конкретной дисциплине
	print('-----------------Статистика по дисциплинам-----------------')
	lessons = list()

	# for i in range(len(dis_p)):
	# 	print(dis_p[i])
	# 	print()

	# for i in range(len(students)):
	# 	print(students[i])
	# 	print()

	for dis1 in range(len(dis_p)):
		count_disl = 0
		students_dis = list()
		tempLesn = dict(name_dis = dis_p[dis1])
		for dis2 in range(len(students)):
			if dis_p[dis1] == students[dis2]['dis']:
				count_disl += students[dis2]['count_mod']
				if students[dis2]['name'] not in students_dis:
					students_dis.append(students[dis2]['name'])
		tempLesn.setdefault('cd', count_disl)
		ltv_dis = count_disl / len(students_dis)
		# print(students_dis)
		# print(count_disl)
		tempLesn.setdefault('ltv_dis', ltv_dis)
		lessons.append(tempLesn)
		# print(lessons)



	v1 = ltv_counch
	v2 = stModCheck / len(students)

	temp_str = ', '.join(dis_p)

	tempp = dict(name = dataTeachers[t]['name'], date_reg = dataTeachers[t]['date'], ID = dataTeachers[t]['id'], LTV_teacher_v1 = v1, LTV_teacher_v2 = v2, dis = temp_str, lessons = lessons)
	ltv_teach_list.append(tempp)

for i in range(len(noStatus)):
	print(noStatus[i])
	print()

for i in range(len(ltv_teach_list)):
	print(ltv_teach_list[i])
	print()

finalData = ltv_teach_list.copy()

workbook = xlsxwriter.Workbook(f'ltv_counch.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
worksheet.write("A1", "ФИО", bold)
worksheet.write("B1", "Дата создания", bold)
worksheet.write("C1", "ID", bold)
worksheet.write("D1", "LTV1", bold)
worksheet.write("E1", "LTV2", bold)
worksheet.write("F1", "Дисциплины", bold)

for i in range(len(finalData)):
	worksheet.write(f'A{i+2}', finalData[i]['name'])

	worksheet.write(f'B{i+2}', finalData[i]['date_reg'])

	ID_teach = 'https://coddy.t8s.ru/Profile/' + str(finalData[i]['ID'])
	worksheet.write(f'C{i+2}', ID_teach)

	worksheet.write(f'D{i+2}', finalData[i]['LTV_teacher_v1'])
	worksheet.write(f'E{i+2}', finalData[i]['LTV_teacher_v2'])

	worksheet.write(f'F{i+2}', finalData[i]['dis'])

workbook.close()



workbook2 = xlsxwriter.Workbook(f'ltv_disciplines.xlsx')
worksheet2 = workbook2.add_worksheet()

bold = workbook2.add_format({'bold': True})
worksheet2.write("A1", "ФИО", bold)
worksheet2.write("B1", "LTV", bold)
worksheet2.write("C1", "Количество модулей на курсе", bold)

for i in range(len(finalData)):
	worksheet2.write(f'A{i+2}', finalData[i]['name'])
	worksheet2.write(f'B{i+2}', finalData[i]['LTV_teacher_v1'])
	for j in range(len(finalData[i]['lessons'])):
		worksheet2.write(f'A{i+2+2+j}', finalData[i]['lessons'][j]['name_dis'])
		worksheet2.write(f'B{i+2+2+j}', finalData[i]['lessons'][j]['ltv_dis'])
		worksheet2.write(f'C{i+2+2+j}', finalData[i]['lessons'][j]['cd'])

workbook2.close()
