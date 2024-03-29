import socket,json

HOST = "127.0.0.1"
PORT = 65432

def general_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    welcome_msg = client_socket.recv(1024).decode('utf-8')
    print(welcome_msg)

    while True:
        visible_answer = input('')
        client_socket.send(visible_answer.encode('utf-8'))
        if visible_answer == 'quit':
            break
        regis_msg = client_socket.recv(1024).decode('utf-8')
        print(regis_msg)
    client_socket.close()
        

if __name__ == "__main__":
    general_client()