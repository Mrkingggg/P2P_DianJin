import socket,json,pickle

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
        print(f"{regis_msg}")


        # conn_msg = client_socket.recv(1024).decode('utf-8')
        # print(f"{conn_msg}")
        
        target_ip = input('input target ip:').strip()
        target_port = int(input('input target port:').strip())
        target_tuple = (target_ip, target_port)
        client_socket.send(pickle.dumps(target_tuple))

        # valid/invalid user feedback:
        feedback = client_socket.recv(1024).decode('utf-8')
        print(feedback)
        
        if feedback != "This user is not available. Change a user or quit.":
           print("succeed!")

        print(client_socket.recv(1024).decode('utf-8'))

    client_socket.close()
        

if __name__ == "__main__":
    general_client()