import socket
import threading
import pickle
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
import queue
import mysql.connector
import re
import os

from cryptography.fernet import Fernet



HOST = "127.0.0.1"
PORT = 65432
msg_queue = queue.Queue()

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root1234"),
    "database": os.getenv("DB_NAME", "p2p")
}

def encrypt_message(message):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def validate_ip(ip_address):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if not re.match(pattern, ip_address):
        raise ValueError("Invalid IP address format.")
        
def validate_port(port):
    if not (0 <= int(port) <= 65535):
        raise ValueError("Port number must be in 0-65535.")


def store_local_messages(msg, target_host, target_port):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    sql = "INSERT INTO offline_msg (targetHost,targetPort, msg) VALUES (%s, %s, %s)"  # number should also use %s
    val = (target_host,target_port,msg)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()


def listen_for_incoming_messages(local_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((HOST, local_port))
        listener.listen()
        while True:
            conn, addr = listener.accept()
            with conn:
                msg = conn.recv(1024).decode('utf-8')
                msg_queue.put(f"Message from {addr[0]}: {msg}")

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
            target_ip = session.prompt('Input target IP host: ')
            target_port = int(session.prompt('Input target port: '))
            client_socket.send(pickle.dumps((target_ip, target_port)))
            feedback = client_socket.recv(1024).decode('utf-8')
            print(feedback)
            if feedback == "This user is not available. Change a user or quit.":
                    message = session.prompt("Enter your message: ")
                    if message.strip():
                        store_local_messages(message, target_ip, target_port)
                        print("Message saved for when the user becomes available.")
                    else:
                        print("No messages to save.")

            else:
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