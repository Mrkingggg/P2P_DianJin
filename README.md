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

### Store message locally:
When the target ip is not available to send messages to, user could select whether or not to send messages. 
#### If choose to send, the message will store in user's local database table, which will record target ip and messages. 
- Store message:
<img width="546" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/857ad5f3-214b-42d2-a62e-1a44337a97af">

- table construct:
<img width="424" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/e150f2d3-34c5-49fd-9c85-083a9633ee4f">

- store result:
<img width="749" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/320ff3f1-61e4-45db-80ef-91ac0e2eb894">

#### If choose not to send, just input return. User could quit or change an ip to chat.
<img width="516" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/f73f36be-9298-4875-9bf4-97a2c36aa203">



### Get Offline: 
When a user get offline and shut down the client thread, the bracket will delete the user's ip record. 
<img width="539" alt="image" src="https://github.com/Mrkingggg/P2P_DianJin/assets/105716817/67f015ea-6210-45a0-91f4-1d6a60435529">
