import socket
from datetime import datetime

def clientProgram():

    # Get the hostname and establish the port number
    # the port number should be the same as the server
    host = socket.gethostname()
    port = 8000

    # Create an instance of the socket object class
    # Connect to server using same port number
    # Input prompt -> saved to message as str
    clientSocket = socket.socket()
    clientSocket.connect((host, port))
    print('Connection Established...')

    message = input(' -> ')
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024).decode()

    # While input is not 'bye', continue to communicate
    # with the server. 'bye' terminates the communication
    # send the message, and then receive the message,
    # print it to the screen, and finally close the
    # connection when 'bye' is entered
    while (data == '--> ERROR: File not found'):
        print('--> ERROR: File not found')
        message = input(' -> ')
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
    print(data)

    # Close the connection with the server
    print('Connection Terminated... ')
    clientSocket.close()

def readFromFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        return None
    content = file.read()
    file.close()
    return content

def makeHTML(contents):
    list = contents.splitlines()
    for i in range(0, len(list)):
        if list[i] == '</body>':
            break
    now = datetime.now()
    ipAddress = "\t<p>My IP Address is " + str(socket.gethostbyname(socket.gethostname())) + "</p>"
    date = "\t<p>Date and Time is " + str(now) + "</p>"
    list.insert(i, date)
    list.insert(i, ipAddress)
    for i in range(0, len(list)):
        print(list[i])

if __name__ == '__main__':
    #clientProgram()
    content = readFromFile('IPAddress.html')
    makeHTML(content)
