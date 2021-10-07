# Import the socket library to allow for network communications
import socket

# Server function, that will serve as the server that listens for
# clients to connect and to request file contents, that the server will
# then send over the sockets that are established
def serverProgram():

    # Get the host name of the device as well as the port number
    # they are going to communicate over
    host = socket.gethostname()
    port = 8000

    # Create an instance of the socket class, and use the bind()
    # function to bind(), since this this a server, bind() must be used
    # to establish the port number, while client doesn't need that
    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    # Set the server to listen for hosts to connect and make requests
    # then once a host connects, server will accept, and connection established
    serverSocket.listen(2)
    connection, address = serverSocket.accept()
    print('Connection Established: ' + str(address))

    # While there is a connection established with client, this loop will continue
    # Client will send data to server, which connection will receive and decode
    # as long as the client data is not None, continue on, serverData will be the
    # file name that the client is trying to get contents of to load on browser
    # If the readFile() returns none, the file doesn't exist, send error message
    # else send to client the file contents
    while True:
        clientData = connection.recv(1024).decode()
        if not clientData:
            break
        serverData = readFromFile(clientData)
        if serverData is None:
            connection.send('--> ERROR: File not found'.encode())
        else:
            connection.send(serverData.encode())

    # Finally close the connection
    print('File contents successfully transfered...')
    print('Connection Terminated: ' + str(address))
    connection.close()

# Read from the file, and if file cannot be found, return None,
# which will prompt client to enter a different file name, otherwise
# will return the file contents, that will be sent back to the client
def readFromFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        return None
    content = file.read()
    file.close()
    return content

# Main function
if __name__ == '__main__':
    serverProgram()