import socket
import sys

host = ''
port = 9999


# Create a socket conect computers
def create_socket():
    try:
        global host, port, s
        s = socket.socket()
    except socket.error as e:
        print("Socket creation error: " + str(e))


# Binding the socket and listening for connections
# create socket has to be called before this function
def bind_socket():
    try:
        global host, port, s
        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as e:
        print("Socket binding error: " + str(e))
        bind_socket()


# function that acepts connections
def socket_accept():
    conn, address = s.accept()
    print("connection has been established with address: " + address[0] + " Port: " + str(address[1]))
    send_comands(conn)
    conn.close()


# function that sends send comands to client
def send_comands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        str_encoded = str.encode(cmd)
        if len(str_encoded) > 0:
            conn.send(str_encoded)
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response)


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == "__main__":
    main()
