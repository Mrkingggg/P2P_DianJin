# import threading, socket

# def recv_cli(sck):
#     while True:
#        try:
#         msg = sck.recv(1024).decode('utf-8')
#         print(msg)
#        except:
#           print("error")
#           sck.close()
#           break

# HOST = "127.0.0.1"
# PORT = 65432

# cli_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cli_serv.connect((HOST, PORT))

# trd = threading.Thread(target=recv_cli, args=(cli_serv,))
# trd.start()

# while True:
#     send_msg = input('')
#     if send_msg == "quit":
#         break
#     cli_serv.send(send_msg.encode('utf-8'))

# cli_serv.close()

import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            sock.close()
            break

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input('')
        if message == 'quit':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

client()
