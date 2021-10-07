import socket

def serverProgram():

    # Get the hostname and establish port number
    host = socket.gethostname()
    port = 8000

    # Create an instance of the socket object class
    # Use bind() function to assign an IP address and port number to socket instance
    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    # Use listen() function to listen for incoming connections
    # Accept function returns two values (host, port) for IPv4
    # and 'accepts' the connection
    serverSocket.listen(2)
    connection, address = serverSocket.accept()
    print('Connection Established: ' + str(address))

    # Now a connection is established between client/server
    # While the client does not terminate the connection,
    # The server will receive data from client, and if the data
    # is not NULL, then the server will send data back to client
    # this will continue until the client terminates the connection
    while True:
        clientData = connection.recv(1024).decode()
        if not clientData:
            break
        serverData = readFromFile(clientData)
        if serverData is None:
            connection.send('--> ERROR: File not found'.encode())
        else:
            connection.send(serverData.encode())

    # Finally, the connection will be closed
    print('Connection Terminated: ' + str(address))
    connection.close()

def readFromFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        return None
    content = file.read()
    file.close()
    return content

if __name__ == '__main__':
    serverProgram()