# Import socket library as well as the datetime
import socket
from datetime import datetime

# Client program, working the client side of the client/server architecture, the client will
# make a request to the server for the html file contents, and once the connection is established
# and the file name is added, the server will return the HTML file contents for it to be changed
def clientProgram():

    # Get the host name and establish the port number the client/server will communicate on
    host = socket.gethostname()
    port = 8000

    # Instance of the socket object, and the connect function call, using host and port number
    # finally, once connection is established, print that the connection is established
    clientSocket = socket.socket()
    clientSocket.connect((host, port))
    print('Connection Established...')

    # The client will prompt to enter a value, this will continue to ask until the name of the
    # HTML file contents are to be downloaded, finally data received is saved as a string
    message = input(' -> ')
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024).decode()

    # While the user does not enter in the HTML file name, the file does not exist, so the
    # error message will be returned each time, until the user enters in 'IPAddress.html'
    # Call send function with the message input by the client through the client socket
    # finally, once the HTML file contents are transferred successfully, call makeHTML()
    while (data == '--> ERROR: File not found'):
        print('--> ERROR: File not found')
        message = input(' -> ')
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
    makeHTML(data)

    # Once the HTML file contents are added, close the connection to the server file
    print('File successfully transfered...')
    print('Connection Terminated... ')
    clientSocket.close()

# The file contents transferred over the clientsocket are then input into makeHTML()
def makeHTML(contents):

    # Make a list of the split lines from the content of the file content transfer
    # and the iterate the list until the </body> is found, then break
    list = contents.splitlines()
    for i in range(0, len(list)):
        if list[i] == '</body>':
            break

    # Now is the date and time of right now according to the computer internal clock
    # then the messages are added to the HTML file contents, according to list index above
    now = datetime.now()
    ipAddress = "\t<p>My IP Address is " + str(socket.gethostbyname(socket.gethostname())) + "</p>"
    date = "\t<p>Date and Time is " + str(now) + "</p>"

    # Insert both into the list, and the join the list together with the join function,
    # finally write the changes to the final.html file
    list.insert(i, date)
    list.insert(i, ipAddress)
    result = '\n'.join(list)
    writeHTML(result)

# Writes the contents from the makeHTML() function to another html file
# that is updated to include date/time and IP address of host
def writeHTML(contents):
    file = open("final.html", "w")
    file.write(contents)
    file.close()

# Main function
if __name__ == '__main__':
    clientProgram()