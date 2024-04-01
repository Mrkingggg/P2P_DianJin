# import socket
# import threading
# import pickle
# import queue

# HOST = "127.0.0.1"
# PORT = 65432
# msg_queue = queue.Queue()

# def listen_for_incoming_messages(local_port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
#         listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         listener.bind((HOST, local_port))
#         listener.listen()
#         while True:
#             conn, addr = listener.accept()
#             with conn:
#                 msg = conn.recv(1024).decode('utf-8')
#                 msg_queue.put((addr, msg))

# def display_messages(stop_event):
#     while not stop_event.is_set():
#         if not msg_queue.empty():
#             addr, msg = msg_queue.get()
#             print(f"\nMessage from {addr[0]}:{addr[1]}: {msg}\nMe: ", end='')

# def send_msg(target_ip, target_port, stop_event):
#     while not stop_event.is_set():
#         send_msg = input("Me:(type 'end' to leave) ")
#         if send_msg.lower() == 'end':
#             stop_event.set()
#             return
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_snd:
#             s_snd.connect((target_ip, target_port))
#             s_snd.send(send_msg.encode('utf-8'))

# def general_client():
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
#     self_ip, self_port = client_socket.getsockname()

#     welcome_msg = client_socket.recv(1024).decode('utf-8')
#     print(welcome_msg)

#     visible_answer = input('')
#     client_socket.send(visible_answer.encode('utf-8'))
#     regis_msg = client_socket.recv(1024).decode('utf-8')
#     print(regis_msg)

#     threading.Thread(target=listen_for_incoming_messages, args=(self_port,), daemon=True).start()

#     while True:
#         target_ip = input('Input target IP: ').strip()
#         target_port = int(input('Input target port: ').strip())
#         client_socket.send(pickle.dumps((target_ip, target_port)))
#         feedback = client_socket.recv(1024).decode('utf-8')
#         print(feedback)

#         if feedback != "This user is not available. Change a user or quit.":
#             stop_event = threading.Event()
#             display_thread = threading.Thread(target=display_messages, args=(stop_event,), daemon=True)
#             display_thread.start()

#             send_msg(target_ip, target_port, stop_event)
#             display_thread.join()  # Wait for display_thread to finish before proceeding

#         choice = input("Quit(enter 0) / Change another user to chat with(enter 1)? ")
#         if choice == '0':
#             client_socket.send('Quit'.encode('utf-8'))
#             client_socket.close()
#             return
#         elif choice != '1':
#             print("Invalid input. Please re-enter.")

# if __name__ == "__main__":
#     general_client()
import socket
import threading
import pickle
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
import queue

HOST = "127.0.0.1"
PORT = 65432
msg_queue = queue.Queue()

def listen_for_incoming_messages(local_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((HOST, local_port))
        listener.listen()
        while True:
            conn, addr = listener.accept()
            with conn:
                msg = conn.recv(1024).decode('utf-8')
                msg_queue.put(f"Message from {addr[0]}:{addr[1]}: {msg}")

def display_messages(session):
    while True:
        if not msg_queue.empty():
            message = msg_queue.get()
            session.app.invalidate()  # Refresh the input area
            print(f"\n{message}")

def general_client():
    session = PromptSession()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    self_ip, self_port = client_socket.getsockname()

    welcome_msg = client_socket.recv(1024).decode('utf-8')
    print(welcome_msg)

    with patch_stdout():
        visible_answer = session.prompt('>')
        client_socket.send(visible_answer.encode('utf-8'))
        regis_msg = client_socket.recv(1024).decode('utf-8')
        print(f"{regis_msg}")

    threading.Thread(target=listen_for_incoming_messages, args=(self_port,), daemon=True).start()

    with patch_stdout():
        while True:
            target_ip = session.prompt('Input target IP: ')
            target_port = int(session.prompt('Input target port: '))
            client_socket.send(pickle.dumps((target_ip, target_port)))
            feedback = client_socket.recv(1024).decode('utf-8')
            print(feedback)

            if feedback != "This user is not available. Change a user or quit.":
                threading.Thread(target=display_messages, args=(session,), daemon=True).start()
                while True:
                    message = session.prompt("Me:(type 'end' to leave) ")
                    if message.lower() == 'end':
                        break
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_snd:
                        s_snd.connect((target_ip, target_port))
                        s_snd.send(message.encode('utf-8'))

            choice = session.prompt("Quit(enter 0) / Change another user to chat with(enter 1)? ")
            if choice == '0':
                client_socket.send('Quit'.encode('utf-8'))
                client_socket.close()
                return
            elif choice != '1':
                print("Invalid input. Please re-enter.")

if __name__ == "__main__":
    general_client()
