import socket
import threading

FORMAT = "utf-8"
PORT = 6741
HOST = '192.168.1.10'
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER.connect((HOST, PORT))

CONNECTED = True


def receive_data():
    global CONNECTED

    while CONNECTED:
        try:
            data = SERVER.recv(1024).decode(FORMAT)
            if data == "200":
                print("Connection established successfully")
            elif data == "404":
                print("Closing client!")
                CONNECTED = False
                SERVER.close()
                break
            else:
                print(data)

        except Exception as err:
            CONNECTED = False
            SERVER.close()
            break


def send_data():
    while CONNECTED:
        data = input(">>")
        SERVER.send(data.encode(FORMAT))


def start_connection():
    receive_thread = threading.Thread(target=receive_data)
    send_thread = threading.Thread(target=send_data)

    receive_thread.start()
    send_thread.start()


start_connection()
