from socket import *
import sys

tcpSerPort = 1080
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
tcpSerSock.bind(('192.168.56.1' , tcpSerPort))
tcpSerSock.listen(1)

while True:
    # Start receiving data from the client
    print 'Ready to serve...'
    tcpCliSock, addr = tcpSerSock.accept()
    print 'Received a connection from: ', addr
	
    try:
		message = tcpCliSock.recv(1024)
		
		print 'message split '+ message
		
		filename = message.split()[1]
		
		f = open(filename[1:])
		outputdata = f.read()
        
		tcpCliSock.send("http/1.1 200 OK\r\n\r\n") #\r\n
        
		for i in range(0, len(outputdata)):
			tcpCliSock.send(outputdata[i])
			
		print 'Request Completed'
		
		tcpCliSock.close()
		
    except IOError:
        #Send response message for file not found
        tcpCliSock.send('404: File Not Found')
        #Close client socket
        tcpCliSock.close()   

tcpSerSock.close()