# В данном случае работа состоит в том, чтобы получить номер из очереди и рассчитать количество циклов до этого числа.
# Оно выводится на консоль, когда начинается цикл, и снова при общем выводе.
# Программа демонстрирует способ, при котором несколько синхронных задач обрабатывают работу в очереди.

import queue

# Данная функция извлекает работу из очереди work_queue и обрабатывает ее до тех пор, пока больше не нужно ничего делать;
def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")

def main():
    """
    Это основная точка входа в программу
    """
    # Создание очереди работы
    work_queue = queue.Queue()

    # Помещение работы в очередь
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Создание нескольких синхронных задач
    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]

    # Запуск задач
    for t, n, q in tasks:
        t(n, q)


if __name__ == "__main__":
    main()

# Задача в данной программе является просто функцией, что принимает строку и очередь в качестве параметров.
# При выполнении она ищет что-либо в очереди для обработки. Если есть над чем поработать, из очереди извлекаются значения,
# запускается цикл for для подсчета до этого значения и выводится итоговое значение в конце.
# Получение работы из очереди продолжается до тех пор, пока на не закончится.

# Здесь показано, что всю работу выполняет Task One. Цикл while, в котором задействован Task One внутри task(), потребляет всю работу в очереди и обрабатывает ее.
# Когда этот цикл завершается, Task Two получает шанс на выполнение.
# Однако он обнаруживает, что очередь пуста, поэтому Task Two выводит оператор, который говорит, что ему нечего делать, и затем завершается.
# В коде нет ничего, что позволяло бы Task One и Task Two переключать контексты и работать вместе.