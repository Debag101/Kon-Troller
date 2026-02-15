import os
import socket
import threading

FORMAT = "utf-8"
PORT = 6741
HOST = socket.gethostbyname(socket.gethostname())
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER.bind((HOST, PORT))
SERVER.listen(1)
SERVER_ON = True

def handle_connection(client, address):
    print(f"Received connection from {str(address)} on port {PORT} ")
    client.send("200".encode(FORMAT))

    while True:
        try:
            data = client.recv(1024).decode(FORMAT)
            if data == "-q":
                client.send("404".encode(FORMAT))
                client.close()
                break
            else:
                print(data)

        except Exception as err:
            print(f"Error | {err}")
            client.close()


def receive_phone_connection():
    print(HOST)
    while SERVER_ON:
        print("Waiting for the connection : ")
        print('Control Head before connection')
        client, address = SERVER.accept()
        print('Control head after connection')
        
        handle_connection_thread = threading.Thread(target=handle_connection, args=(client, address ))
        handle_connection_thread.start()


if __name__ == '__main__':
    receive_phone_connection()