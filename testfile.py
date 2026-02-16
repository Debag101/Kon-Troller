import socket
import threading
import time

HOST = '255.255.255.255'
PORT = 6741

CONNECTED = False

#Creating a dgram (Data Gram) socket, DG = Drain Gang
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Changing socket options to be a broadcast
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#client_socket.settimeout(5)
        
def sendto_host():
    while CONNECTED:
        print("CONNECTED!")
        client_socket.sendto('pinging host'.encode('utf-8'), (HOST, PORT))
        time.sleep(3)

def find_pc():
    global CONNECTED
    global HOST

    while not CONNECTED:
        #print('here1')
        data = 'controller'
        client_socket.sendto(data.encode('utf-8'), (HOST, PORT))
        #print('here2')
        reply, address = client_socket.recvfrom(1024)

        reply = reply.decode('utf-8')
        print(reply)

        if reply == 'fedora':
            CONNECTED = True
            HOST = address[0]

            client_socket.sendto('connect'.encode('utf-8'), address)
            print(f'Connected to -> {reply} at address {address}')
            sendto_host_thread = threading.Thread(target=sendto_host, args=())
            sendto_host_thread.start()

            break
        time.sleep(3)



def main():

    find_pc_thread = threading.Thread(target=find_pc, args=())
    find_pc_thread.start()

main()

