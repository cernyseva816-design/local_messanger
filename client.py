import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.111', 8888))

print("Подключено к серверу. Введите сообщения (для выхода — 'exit')")

try:
    while True:
        message = input("Вы: ")
        if message.lower() == 'exit':
            break

        s.send(message.encode('utf-8'))

        response = s.recv(1024)
        if not response:  # если сервер закрыл соединение
            print("Сервер закрыл соединение.")
            break

        print(f"Сервер: {response.decode('utf-8')}")

except KeyboardInterrupt:
    print("\nКлиент прерван пользователем.")

finally:
    s.close()
    print("Соединение закрыто.")
    print('shkebob')