import socket

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
    message = input(' -> ')

    # While input is not 'bye', continue to communicate
    # with the server. 'bye' terminates the communication
    # send the message, and then receive the message,
    # print it to the screen, and finally close the
    # connection when 'bye' is entered
    while (message.lower().strip() != 'bye'):
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
        print( 'Received from server: ' + data )
        message = input(' -> ')

    # Close the connection with the server
    clientSocket.close()

if __name__ == '__main__':
    clientProgram()