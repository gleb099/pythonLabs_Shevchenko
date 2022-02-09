import random

def createTable(width):
    table=list(range(width))
    for i in range(0, width):
        table[i] = [random.randint(10, 99) for x in range(width)]
    return table

def printTable():
    for i in table:
        print(*i)

def rotateTable(right: bool):
    if(right):
        return list(zip(*table[::-1]))
    else:
        return list(zip(*table))[::-1]

def mirror(vert: bool):
    if(vert):
        return table[::-1]
    else:
        return list(zip(*list(zip(*table[::-1]))[::-1]))[::-1]

def transp():
    return list(zip(*table))

if __name__ == "__main__":
    table = createTable(10)
    printTable()

    print("1 - поворот влево")
    print("2 - поворот вправо")
    print("3 - отразить горизонтально")
    print("4 - отразить вертикально")
    print("5 - транспонировать")

    number=int(input())
    if(number==1):
        table=rotateTable(False)
    elif(number==2):
        table=rotateTable(True)
    elif(number==3):
        table=mirror(False)
    elif(number==4):
        table=mirror(True)
    elif(number==5):
        table=transp()
    printTable()

