# Peer To Peer chatting room

## Overview
- Registration: When a client thread connects to the server, this ip address is added into the ip bracket. Bracket not be stored in server.
- Discovery: User choose whether or not to be discovered by other users. The answer: True/False will be recorded together with ip address in the bracket. When others are searching some ip, if this ip is with 'False', then this ip is not available. Otherwise with a True, this user is available and others could send message to this user.
- Offline: When a user get offline and shut down the client thread, the bracket will delete the ip record. 
