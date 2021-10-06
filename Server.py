import socket

def serverProgram():
    host = socket.gethostname()
    port = 8000

    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(2)
    connection, address = serverSocket.accept()
    print('Connection from ' + str(address))
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print('From connected user: ' + str(data))
        data = input(' -> ')
        connection.send(data.encode())
    connection.close()

if __name__ == '__main__':
    serverProgram()