import socket
import threading,pickle

HOST = "127.0.0.1"
PORT = 65432

import socket
import threading

def thread_chat(client_socket, client_addr, clients, lock):
    try:
        while True:
            data = client_socket.recv(1024)
            # if not data:
            #     break
            visibility = data.decode('utf-8')
            if visibility.lower() == 'quit':
                break
            with lock:
                clients[client_addr] = visibility  
                print(f"client {client_addr}: {visibility}, Registered Successfully")
                client_socket.send("Registered Successfully\n".encode('utf-8'))
                print(f"online users:{clients}")
            
            client_socket.send("To which IP address you want to send message?\n".encode('utf-8'))
            tar_addr = pickle.loads(client_socket.recv(1024))
            
            client_socket.send("receive port !".encode('utf-8'))
            print(tar_addr)
            while tar_addr not in clients:
                client_socket.send("This user is not available. Change a user or quit.".encode('utf-8'))
                tar_addr = client_socket.recv(1024).decode('utf-8')
            #     if tar_addr.lower() == 'quit':
            #         break
            
            # if tar_addr.lower() == 'quit':
            #     break
            client_socket.send(f"user {tar_addr} is available. Send message now!")
    finally:
        with lock:
            if client_addr in clients:
                del clients[client_addr]
                print(f"client {client_addr} has been removed.")
                print(f"online users:{clients}")
        client_socket.close()


def general_chat():
    print("server starting...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    clients = {}  # map: record ip and visibility
    lock = threading.Lock() 
    
    print("Server listening on port 65432")

    while True:

        client_socket, client_addr = server_socket.accept()

        client_socket.send(f"Welcome: {client_addr}! Do you want to be discovered by others?(True/False) If want to quit the chatting system, enter quit.".encode('utf-8'))

        thread = threading.Thread(target=thread_chat, args=(client_socket, client_addr, clients, lock))
        thread.start()

if __name__ == "__main__":
    general_chat()
