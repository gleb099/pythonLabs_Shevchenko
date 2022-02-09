import random
import time

def getTime(level):
    if level == 1:
        h1, h2 = random.randint(0, 1), random.randint(0, 1)
        m1, m2 = random.randrange(1, 60, 5), random.randrange(1, 60, 5)
    elif level == 2:
        h1, h2 = random.randint(0, 3), random.randint(0, 3)
        m1, m2 = random.randrange(1, 60, 5), random.randrange(1, 60, 5)
    elif level == 3:
        h1, h2 = random.randint(0, 8), random.randint(0, 8)
        m1, m2 = random.randrange(1, 60, 5), random.randrange(1, 60, 5)
    elif level == 4:
        h1, h2 = random.randint(0, 23), random.randint(0, 23)
        m1, m2 = random.randrange(1, 60, 5), random.randrange(1, 60, 5)

    return ((h1, h2), (m1, m2))

def getRes(h1, m1, h2, m2):
    mm1 = h1 * 60 + m1
    mm2 = h2 * 60 + m2
    resMM = mm1 + mm2
    if (resMM % 60) < 10:
        resHM = f"{resMM // 60}:0{resMM % 60}"
    else:
        resHM = f"{resMM // 60}:{resMM % 60}"
    if resMM < 10:
        resMM = f"0{resMM}"
    return (f"{resMM}", resHM)

print("Уровни сложности:\n1. Детский\n2. Легкий\n3. Средний\n4. Сложный\n")

level = int(input("Введите желаемый уровень сложности "))
countQues = int(input("Введите количество вопросов "))
print()
right = 0
start_time = time.time()

for i in range(countQues):
    h1, h2 = getTime(level)[0]
    m1, m2 = getTime(level)[1]

    mode = random.randint(1, 2)
    if mode == 2:
        mode = "HH:MM"
        realRes = getRes(h1, m1, h2, m2)[1]
    else:
        mode = "MM"
        realRes = getRes(h1, m1, h2, m2)[0]

    print(f"{h1}:{m1} + {h2}:{m2} = ? {mode}")
    userRes = input("Ответ: ")

    if userRes == realRes:
        right+=1

print("Итоги")
print(f"Время игры {round(time.time()-start_time, 3)}")
print(f"Количество правильных ответов {right}")
print(f"Количество неправильных ответов {countQues-right}")

