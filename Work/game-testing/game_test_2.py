# Douglas Wise
# client-server in python
# October 21, 2017

from socket import *
import os.path

serverPort = 12000
serverSocket = 0
path = "./store/game_state.txt"

def main():
    client_server_select = raw_input('Type client or server: ')

    if client_server_select == 'client':
        client()
    elif client_server_select == 'server':
        server()
    else:
        print 'Invalid option. Closing.'

def client():
    serverName = raw_input('Enter server IP: ')

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print 'Client started.\nValid command is send\nEnter \'q\' to quit.'

    while 1:
        command = clientSocket.recv(1024)
        if command == 'q':
            break
        elif command == 'send':
            clientSocket.send('send file')
            fileMessage = clientSocket.recv(1024)
            test = fileMessage.split(":", 1)
            if test[0] == "Failure":
                print fileMessage
            else:
                f = open(path, 'wb')
                while fileMessage:
                    f.write(fileMessage)
                    fileMessage = clientSocket.recv(1024)
                print 'Receive complete.'
                f.close()
        else:
            print 'bad command'

        client_command = raw_input('Player 2: ')
        if client_command == 'q':
            break

        elif client_command == 'send':
            clientSocket.send(client_command)
            if clientSocket.recv(1024) == 'send file':
                sendFile(clientSocket)
                clientSocket.shutdown(SHUT_WR)
            else:
                print 'no ack'
        else:
            print 'bad command'

    clientSocket.close()

def server():
    global serverSocket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print "The server has started.\nUse ctrl-c to quit."
    connectionSocket, addr = serverSocket.accept()

    while 1:
        command = raw_input('Player 1: ')

        if command == 'q':
            break

        elif command == 'send':
            connectionSocket.send(command)
            if connectionSocket.recv(1024) == 'send file':
                sendFile(connectionSocket)
                connectionSocket.shutdown(SHUT_WR)
            else:
                print 'no ack'
        else:
            print 'bad command'

        server_command = connectionSocket.recv(1024)
        if server_command == 'send':
            connectionSocket.send('send file')
            fileMessage = connectionSocket.recv(1024)
            test = fileMessage.split(":", 1)
            if test[0] == "Failure":
                print fileMessage
            else:
                f = open(path, 'wb')
                while fileMessage:
                    f.write(fileMessage)
                    fileMessage = connectionSocket.recv(1024)
                print 'Receive complete.'
                f.close()
        else:
            print 'bad command'


    connectionSocket.close()

def send(user, socket):
    command = raw_input(user + ': ')

    #checks for quit command
    if command == 'q':
        print 'Quiting'
        socket.send(command)    #sends quit command
        # socket.shutdown(SHUT_WR)        #done sending
        return 0                #returns. nothing sent

    #checks if "player 1" wants to send
    elif command == 'send':
        socket.send(command)         #sends send notification
        # socket.shutdown(SHUT_WR)        #done sending
        request = socket.recv(1024)         #waits for ack
        if request == 'send file':          #if ack
            sendFile(socket)                #sends file
            socket.shutdown(SHUT_WR)        #done sending
            print 'Send Complete'           #user notification
            return 1                        #successful return
        else:
            print 'request failed'
    #bad command notification
    else:
        print 'Bad command: ' + command


def recieve(socket):
    print 'Waiting for input from opponent'
    #recieves command
    command = socket.recv(1024)

    #opponent quit
    if command == 'q':
        print 'opponent quit'
        return 0

    #recieve send request
    elif command == 'send':
        socket.send('send file')            #send ack
        # socket.shutdown(SHUT_WR)        #done sending
        fileMessage = socket.recv(1024)     #get file
        test = fileMessage.split(":", 1)    #split for testing
        if test[0] == "Failure":            #test for failed recieve
            print fileMessage

        else:                               #didn't fail
            f = open(path, 'wb')            #open file for writing
            while fileMessage:              #write to file
                f.write(fileMessage)
                fileMessage = socket.recv(1024)
            print 'Receive complete.'
            f.close()                       #close file
            return 1
    #bad command notification
    else:
        print ('Bad command: '+ command)
        socket.send('Bad command')
        # socket.shutdown(SHUT_WR)        #done sending


def sendFile(sock):
    if not os.path.isfile(path):
        message = 'Failure: no file'
        sock.send(message)
        print message
        return
    f = open(path, 'rb')
    l = f.read(1024)
    while l:
        sock.send(l)
        l = f.read(1024)
    f.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Closing.'
        serverSocket.shutdown(SHUT_RDWR)
        serverSocket.close()
