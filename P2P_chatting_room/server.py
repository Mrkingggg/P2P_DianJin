# import socket
# import threading,pickle

# HOST = "127.0.0.1"
# PORT = 65432

# import socket
# import threading

# def thread_chat(client_socket, client_addr, clients, lock):
#     try:
#         while True:
#             data = client_socket.recv(1024)
#             # if not data:
#             #     break
#             visibility = data.decode('utf-8')
#             if visibility.lower() == 'quit':
#                 break
#             with lock:
#                 clients[client_addr] = visibility  
#                 print(f"client {client_addr}: {visibility}, Registered Successfully")

#                 client_socket.send("Registered Successfully.\nTo which IP address you want to send message?\n".encode('utf-8'))
#                 print(f"online users:{clients}")
            
#             # client_socket.send("To which IP address you want to send message?".encode('utf-8'))
#             if client_socket.recv(1024).decode('utf-8')=="Quit":
#                 break
#             tar_addr = pickle.loads(client_socket.recv(1024))
            
#             # client_socket.send("receive port !".encode('utf-8'))
#             print(tar_addr)
#             send_msg = "This user is not available. Change a user or quit."
#             while tar_addr not in clients:
#                 client_socket.send(send_msg.encode('utf-8'))
#                 tar_addr = pickle.loads(client_socket.recv(1024))
#             while clients[tar_addr]=='False':
#                 client_socket.send(send_msg.encode('utf-8'))
#                 tar_addr = pickle.loads(client_socket.recv(1024))

#             client_socket.send("user is available. Send message now!\n".encode('utf-8'))
           
#     finally:
#         with lock:
#             if client_addr in clients:
#                 del clients[client_addr]
#                 print(f"client {client_addr} has been removed.")
#                 print(f"online users:{clients}")
#         client_socket.close()


# def general_chat():
#     print("server starting...")
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen()
#     clients = {}  # map: record ip and visibility
#     lock = threading.Lock() 
    
#     print("Server listening on port 65432")

#     while True:

#         client_socket, client_addr = server_socket.accept()

#         client_socket.send(f"Welcome: {client_addr}! Do you want to be discovered by others?(True/False) If want to quit the chatting system, enter quit.".encode('utf-8'))

#         thread = threading.Thread(target=thread_chat, args=(client_socket, client_addr, clients, lock))
#         thread.start()

# if __name__ == "__main__":
#     general_chat()
import socket
import threading
import pickle

HOST = "127.0.0.1"
PORT = 65432

def thread_chat(client_socket, client_addr, clients, lock):
    try:
        visibility = client_socket.recv(1024).decode('utf-8').lower()
        if visibility == 'quit':
            return

        with lock:
            clients[client_addr] = visibility == 'true'
            print(f"client {client_addr}: visibility set to {visibility}, registered successfully")
            client_socket.send("Registered successfully. To which IP address you want to send a message?".encode('utf-8'))

        while True:
            tar_addr = pickle.loads(client_socket.recv(1024))
            if tar_addr in clients and clients[tar_addr]:
                client_socket.send("User is available. Send message now!\n".encode('utf-8'))
                # Here should be logic to handle message passing between clients
            else:
                client_socket.send("This user is not available. Change a user or quit.".encode('utf-8'))
            
    finally:
        with lock:
            if client_addr in clients:
                del clients[client_addr]
                print(f"client {client_addr} has been removed.")

def general_chat():
    print("Server starting...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    clients = {}
    lock = threading.Lock()

    print(f"Server listening on port {PORT}")

    while True:
        client_socket, client_addr = server_socket.accept()
        welcome_message = "Welcome! Do you want to be discovered by others? (True/False) To quit, enter 'quit'."
        client_socket.send(welcome_message.encode('utf-8'))

        threading.Thread(target=thread_chat, args=(client_socket, client_addr, clients, lock)).start()

if __name__ == "__main__":
    general_chat()