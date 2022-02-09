import threading

def print_cube(num):
    print(f"Cube: {num * num * num}")

def print_square(num, num2):
    print(f"Square: {num * num2}")

if __name__ == "__main__":
    # создаем потоки
    t1 = threading.Thread(target=print_square, args=(10,15,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    #запускаем их и ждем пока они завершат работу
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")