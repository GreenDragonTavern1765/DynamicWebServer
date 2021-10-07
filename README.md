# DynamicWebServer
## Computer Networks and Communications (Lab 4): Create a Dynamic Web Server
Write a program that listens on a TCP port specified at run time. When a connection is made, the server will send back an HTTP 200 response and HTML text, which when shown in a browser, will display:

"Your IP address is- " followed by the IP address of the machine that has connected. The IP address of the client may be obtained using the getInetAddress method in the Socket class.

## Client.py File
Importing the socket library as well as the datetime library. Socket library needed for the computer to establish a socket to communicate over the network, whereas datetime is used to get the current date and time as a string from the computer's internal clock.

**clientProgram()**

Get the host name and the port number, which will then be used to connect to the server over the established port number, in this case we are using port number 8000. Once the connection is established, the client will be prompted to type a message (->). The client will type 'IPAddress.html' which is the file that contains the contents the client wants. Until the file name is established over the sockets, the server will continue to prompt the client. Once the fileName is entered, the file contents are then read off from the server and sent to the client as one string, at which point the client will add the additional information, such as IP address and date/time information.

**makeHTML(contents)**

File contents transferred over the sockets are the input into this function to create the HTML file that will be loaded into the browser. The contents is split by line and saved in a list. The list is iterated through a loop until </body> is found. The two strings to be added, along with the <p></p> are added to the string. Then the list is joined back together again, and the contents are ready to be written to the file.

**writeHTML(contents)**

Write the contents from the makeHTML() function to another HTML file that is updated to include the date/time information as well as the IP address of the host.

## Server.py File
Importing the socket library. The socket library is needed for the computer to establish a socket to communicate over the network.

**serverProgram()**

Server functio that will serve as the server that listens for clients to connect and to make requests for file contents, in this case the IPAddress.html file, which will be added to by the client file. First, get the host name as well as the port number that will be communicated over. Create an instance of the socket class, and use bind() function to bind(). Because this is the server and not the client, bind() function is necessary to establish the port number to be communicated over, which the client doesn't need it. Set the server to listen for hosts to connect and make requests for file contents. Server will accept and connection established. While there is a connection established, continue to receive data from the client, and evaluate the data returned over sockets. The data is the file name of the HTML file that the client wants the contents of. If the client does not enter the file name, the contents cannot be sent, the client must be prompted again to enter the file name. Finally once the file is entered, the serverdata is loaded with the file contents, and sent back throught sockets to the client. Finally close the connections.

**readFromFile(fileName)**

Read from the file, and if file cannot be found, return None, which will prompt the client to enter a different file name, otherwise will return the file contents, that will be sent back to the client over the sockets.

## IPAddress.html and final.html
HTML file that contains basic web page text, more to be added once the client gets the contents of the file. final.html is the same as IPaddress.html, the only difference is final.html is updated to include the IP address of the host that is creating it as well as the date/time of the localhost, according to it's internal clock.
