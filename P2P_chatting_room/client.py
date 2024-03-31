import socket
import threading
import pickle

HOST = "127.0.0.1"
PORT = 65432

def listen_for_incoming_messages(local_port):
    # Set up a listening socket to receive incoming messages
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((HOST, local_port))
        listener.listen()

        while True:
            conn, addr = listener.accept()
            with conn:
                msg = conn.recv(1024)
                print(f"\nMessage from {addr[0]}:{addr[1]}: {msg.decode('utf-8')}\nMe: ", end='')

def general_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    self_ip, self_port = client_socket.getsockname()  # client's self host & port

    welcome_msg = client_socket.recv(1024).decode('utf-8')
    print(welcome_msg)
    visible_answer = input('')
    if visible_answer == 'quit':
        client_socket.close()
    client_socket.send(visible_answer.encode('utf-8'))
    regis_msg = client_socket.recv(1024).decode('utf-8')
    print(f"{regis_msg}") # registration success

    # Start listening thread for incoming messages
    threading.Thread(target=listen_for_incoming_messages, args=(self_port,), daemon=True).start()

    while True:

        while True: 
            # check target ip availibility
            target_ip = input('Input target IP: ').strip()
            target_port = int(input('Input target port: ').strip())
            target_tuple = (target_ip, target_port)
            client_socket.send(pickle.dumps(target_tuple))
            feedback = client_socket.recv(1024).decode('utf-8')
            print(feedback)
            if feedback != "This user is not available. Change a user or quit.":
                break

        # Chat with target ip
        while True:
            send_msg = input("Me:(end to leave)")
            if send_msg == 'end':
                s_snd.close()
                break
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_snd:
                s_snd.connect((target_ip, target_port))
                s_snd.send(send_msg.encode('utf-8'))

        # client exits or change target ip
        while True: 
            choice = int(input("Quit(enter 0) / Change another user to chat with(enter 1)?"))
            if choice==0:
                client_socket.close()
                end_msg = "Quit"
                client_socket.send(end_msg.encode('utf-8'))
                break
            elif choice==1:
                break # start chat with another user
            else:
                print("invalid input. Re-enter.")


if __name__ == "__main__":
    general_client()
