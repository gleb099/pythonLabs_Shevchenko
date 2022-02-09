import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 80 # порт 80 может слететь

clients = [] # принимаем адреса клиентов, а не usernames

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # s содержит сокеты, сначала ТСП, потом АЙПИ
s.bind((host, port)) #именно на этом хосте будет поднят сервер, и на этом порте работаем

running = False

print('[ Server Started ]')

while not running:
    try:
        data, addr = s.recvfrom(1024) #отправили и приняли по адресам и сервер может принимать до 1Кб

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime()) #время отправления

        print('[' + addr[0] + ']=[' + str(addr[1]) + ']=[' + itsatime + ']/', end = '')
        print(data.decode('utf-8'))

        for client in clients:
            if addr != client:
                s.sendto(data, client) #если клиент другой, то отправляем, если нет, то не отправляем

    except:
        print('\n[ Server Stopped ]')
        running = True

s.close()