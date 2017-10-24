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

    # while 1:
    #     recieved = recieve(clientSocket)
    #     if recieved == 0:
    #         break
    #     else:
    #         sent = send('Player 2', clientSocket)
    #         if sent == 0:
    #             break


    recieve(clientSocket)

    send('Player 2', clientSocket)

    clientSocket.close()

def server():
    global serverSocket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print "The server has started.\nUse ctrl-c to quit."
    connectionSocket, addr = serverSocket.accept()
    # while 1:
    #     sent = send('Player 1', connectionSocket)
    #     if sent == 0:
    #         break
    #     else:
    #         recieved = recieve(connectionSocket)
    #         if recieved == 0:
    #             break

    send('Player 1', connectionSocket)

    recieve(connectionSocket)

    connectionSocket.close()

def send(user, socket):
    command = raw_input(user + ': ')

    #checks for quit command
    if command == 'q':
        print 'Quiting'
        socket.send(command)    #sends quit command
        return 0                #returns. nothing sent

    #checks if "player 1" wants to send
    elif command == 'send':
        socket.send(command)         #sends send notification
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
