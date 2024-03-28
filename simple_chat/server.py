# import socket, threading

# HOST = "127.0.0.1"
# PORT = 65432


# def recv_cli(cli, cli_addr):
#     while True:
#         try:
#             msg = cli.recv(1024).decode('utf-8')
#             if not msg:
#                 break

#             for other in clients:
#                 if other != cli:
#                     try:
#                         other.send(f"{cli_addr} said: {msg}.")
#                     except:
#                         clients.remove(other)
#                         other.close()

#         except:
#             clients.remove(cli)
#             cli.close()
#             break

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))

# server.listen()

# clients = set()

# while True: 
#     cli, cli_addr = server.accept()
#     clients.add(cli)
#     thread = threading.Thread(target=recv_cli, args=(cli, cli_addr))
#     thread.start()

import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            for other_client_socket in clients:
                if other_client_socket != client_socket:
                    try:
                        other_client_socket.send(f"{client_address}: {message}".encode('utf-8'))
                    except:
                        clients.remove(other_client_socket)
                        other_client_socket.close()
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen()

    print("Server listening on port 65432")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        clients.add(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

clients = set()
server()

