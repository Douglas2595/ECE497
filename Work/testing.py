#!/usr/bin/env python3
#Douglas Wise
#Sep 18, 2017
#testing file

# test = input('input: jpeg ')
# if test == 'jpeg':
#     print('pass')
# else:
#     print('fail')


#map testing
# a = "a"
# b = "b"
#
# map1 = {a: 'A', b: 'B'}
# map2 = {a: 1, b: 2}
#
# print("Begin Test")
# print("testing map a: {} and {}".format(map1[a], map2[a]))
# print("testing map b: {} and {}".format(map1[b], map2[b]))
# print("Test Finished")

#or testing
# a = 0x10
# b = 0x01
#
# y = a | b
# print('y = {}'.format(format(y, '02x')))

#bit shift testing
# a = 0x01
# for i in range(1, 5):
#     print('a = {}'.format(format(a, '02x')))
#     a = a << 1

#subprocess testing
# import subprocess
#
# subprocess.run('ls')

#terminal line clearing
# import time
# while 1:
#     print("blah", end="\r")
#     time.sleep(0.5)
#     print("haaablah", end = "\r", flush=True)
#     time.sleep(0.5)
#     print("           ", end = "\r")
#     time.sleep(0.5)

#using curses to end program
# import curses, sys, time
#
# stdscr = curses.initscr()
# stdscr.nodelay(1)
#
# def esc():
#     curses.endwin()
#     sys.exit()
#
# i = 0
# while 1:
#     time.sleep(0.5)
#     key = stdscr.getch()
#     print("Running... count: {}".format(i), end = "\r")
#     i += 1
#     if key == 27:
#         esc()

while 1:
    sent = send('Player 1', socket)
    if sent == 0:
        break
    else:
        recieved = recieve(socket)
        if recieved == 0:
            break



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
