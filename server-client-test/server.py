from socket import AF_INET, SOCK_STREAM, socket, SOCK_DGRAM
import threading  # multi-thread execution of code to make certain blocks run in parallel regardless of order.
import time
import sys

server = socket(AF_INET, SOCK_DGRAM)
host = sys.argv[1]  # This line should ideally be the IP address of the network user is currently connected to.
# e.g host = socket.gethostbyname(socket.gethostname())
port = 9999
buf = 4096
addr = (host, port)



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} ")
    connected = True
    while connected:
        msg = conn.recv()



def start():
    server.listen()
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client(conn, address), args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


server.connect((host, port))

file_name = sys.argv[2]

f = open(file_name, "rb")
data = f.read(buf)
print('Sending file ' + file_name + ' ...')

print("[STARTING] server is starting...")
start()

sent_size = 0

while True:
    if server.send(data):

        sent_size += buf
        mb = round(sent_size / 1024 / 1024, 2)
        sys.stdout.write("\rSent: " + str(mb) + " MB")
        sys.stdout.flush()

        time.sleep(0.001)
        data = f.read(buf)

    else:
        print('\n- Finished')
        server.close()
        break
