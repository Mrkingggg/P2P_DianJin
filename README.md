# Peer To Peer chatting room

### Server starts:
<img width="529" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/8c790ee1-0e41-41dd-b040-d2b5701a54b0">


### Registration: 
When a client thread connects to the server, this ip address is added into the ip bracket. Bracket not be stored in server. The discorvery(visibility) also recorded.

<img width="1169" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/5dba8538-00c5-4832-b0cb-96c89fd4b365">


### Discovery: 
User choose whether or not to be discovered by other users. The answer: True/False will be recorded together with ip address in the bracket. When others are searching some ip, if this ip is with 'False', then this ip is not available. Otherwise with a True, this user is available and others could send message to this user.

<img width="1169" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/aca60a70-2985-4fad-9842-25e82e14964e">

### Select an IP address and Chat:
- After the registration with discovery availability, user could input an ip (host and port). If the target ip is online and available, then user could send message.
- During the input for target ip selecting, the process is blocked and will not display messages from other users.
- After connecting to the target ip, the user terminal will display all messages store in the message queue from other users.
- When inputting messages to target ip, user could also receive and see messages real time from others. But user's current inputting will not be disturbed, owe to python prompt kit
<img width="1194" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/6ee0ec79-3191-4250-b0b5-f2da6f463100">

### Change user to chat with:

<img width="372" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/fbe2a7f9-327b-4049-a8a2-2647898fa782">

### Quit the chatting system:

<img width="369" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/5eff1392-2f5f-4ce0-bb23-e969d829184e">


### Offline: 
When a user get offline and shut down the client thread, the bracket will delete the user's ip record. 
<img width="539" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/67f015ea-6210-45a0-91f4-1d6a60435529">
