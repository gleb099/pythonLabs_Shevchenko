import socket, threading, time

# добавили еще многопотчность, чтобы не получать сообщение после отправки

# ключ для шифровки
key = 8194

shutdown = False
join = False


# для приема данных
def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                # print(data.decode('utf-8'))

                decrypt = '';
                k = False
                for i in data.decode('utf-8'):
                    if i == ':':
                        k = True
                        decrypt += i
                    elif k == False or i == ' ':
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)
                # END OF DECRYPT

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('172.20.10.8', 80)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)  # чтобы без ошибок, хотя бы чтобы выйти

name = input('Name: ')

rT = threading.Thread(target=receving, args=('RecvThread', s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(('[' + name + '] => join chat ').encode('utf-8'), server)
        join = True

    else:
        try:
            message = input()

            # BEGIN CRYPT csor - шифрование

            crypt = ''
            for i in message:
                crypt += chr(ord(i) ^ key)
            message = crypt

            # END OF CRYPT

            if message != '':
                s.sendto(('[' + name + '] :: ' + message).encode('utf-8'), server)

            time.sleep(0.2)

        except:
            s.sendto(('[' + name + '] <= left chat').encode('utf-8'), server)
            shutdown = True

rT.join()  # для нормального контакт по времени между пользователями
s.close()