import socket
import sys
import os

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
RECEIVE_FILE_EXTENSION = ['.zip', '.mp4', '.png', '.obj', '.fbx', '.glb']
SENDING_FILE_EXTENSION = '.blend'


'''def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


def send_file():
        filename= input('Enter File name:')
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                s.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                s.close()
                break

def receive_render():
    with open(f'received_file', 'wb') as f:
        print('[SUCCESS] File opened')
        received_data = 0
        while True:
            print('[PROCESS] Receiving data...')
            received_data += BUFFER_SIZE # Increment each buffer sent and convert to mb to find amount recieved
            mb = round(received_data / 1024 / 1024, 2) # mb = total buffer load sent / (1024/1024/2)
            print("\rReceived: " + str(mb) + " MB")



            data = s.recv(BUFFER_SIZE) #



            if not data:
                f.close()
                print ('File closed')
                break
            # write data to a file
            f.write(data)

    print('Successfully get the file')
    s.close()
    print('connection closed')


receive_render()