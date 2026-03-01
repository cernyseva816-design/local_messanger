import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
s.listen(1)

print("Сервер запущен. Ожидание подключения...")

try:
    client, addr = s.accept()
    print(f"Подключен клиент: {addr}")

    while True:
        data = client.recv(1024)
        if not data:  # клиент закрыл соединение
            print("Клиент отключился.")
            break

        message = data.decode('utf-8')
        print(f"Клиент: {message}")

        response = f"Вы сказали: '{message}'"
        client.send(response.encode('utf-8'))

except KeyboardInterrupt:
    print("\nСервер остановлен.")

finally:
    client.close()
    s.close()
    print("Сервер закрыт.")