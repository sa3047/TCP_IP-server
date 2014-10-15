from socket import *
import sys

tcpSerPort = 1080
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
tcpSerSock.bind(('192.168.56.1' , tcpSerPort))

#This will receive 10 clients connection
tcpSerSock.listen(10)

while True:
    # Start receiving data from the client
    print 'Ready to serve...'
    tcpCliSock, addr = tcpSerSock.accept()
    print 'Received a connection from: ', addr
	
    try:
		message = tcpCliSock.recv(4096)
		
		print 'message split '+ message
		
		filename = message.split()[1]
		print 'file name  -> '+ filename[1:]
		f = open(filename[1:])
		outputdata = f.read()
        
		print 'output data '+ outputdata
		
		tcpCliSock.send(outputdata)
		
		'''for i in range(0, len(outputdata)):
			tcpCliSock.send(outputdata[i])'''
		
		tcpCliSock.send("http/1.1 200 OK\r\n\r\n") #\r\n

		
			
		print 'Request Completed'
		
		tcpCliSock.close()
		
    except IOError:
        #Send response message for file not found
		tcpCliSock.send('404: File Not Found')
        #Close client socket
		tcpCliSock.close()   

tcpSerSock.close()