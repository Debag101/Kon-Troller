import socket
import threading

HOST = '0.0.0.0'
PORT = 6741

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))


def accept_connection():
    while True:
        data, ret_address = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print(data)
        if data == 'controller':
            sock.sendto(f"{socket.gethostname()}".encode('utf-8'), ret_address)
        

connection_thread = threading.Thread(target=accept_connection, args=())
connection_thread.start()
    
