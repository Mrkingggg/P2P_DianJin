# Simple Chat Room

This project includes a simple chat server and client implemented in Python. The server can handle multiple client connections, receiving messages from one client and broadcasting them to all other clients. It's an illustrative example of basic networking and multi-threading in Python.

## Getting Started

## Server

### Overview

The server listens for incoming connections on port 12345 and handles each client in a separate thread. It receives messages from any connected client and broadcasts these messages to all other clients.

### Running the Server

   ```bash
   python server.py
   ```
## Client

### Overview

- Connects to the chat server
- Sends messages to the server for broadcasting
- Displays messages from other clients
### Running the Server

   ```bash
   python client.py

   ```

- result:
  
<img width="1355" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/ff48270d-3a09-41df-aa36-d83d7ffd9bb9">

<img width="1236" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/67658581-b839-4097-94ae-84b0df6905d9">
