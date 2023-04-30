This is a simple chat application built in Python using the socket library. The application consists of a server that listens to incoming connections from multiple clients, and a client that connects to the server and allows the user to send and receive messages.
<br>
The server listens to incoming connections on port 9090. When a new client connects, the server sends a "NICK" message to the client, prompting the client to enter a nickname. Once the client enters a nickname, the server broadcasts a message to all connected clients that a new user has joined the chat.

The client connects to the server and prompts the user to enter a nickname. Once the user enters a nickname, the client opens a chat window where the user can send and receive messages. When the user sends a message, the client sends the message to the server, which broadcasts the message to all connected clients.


## Server
The server file server.py creates a server that listens on port 9090 for incoming client connections. It uses the socket module to create a socket and bind it to a specific address and port. It then listens for incoming connections using the listen method.

The server uses the threading module to create a new thread for each incoming client connection. Each thread runs the handle function which receives messages from the client and broadcasts them to all other connected clients. The clients and nicknames lists are used to keep track of connected clients and their respective nicknames.

The broadcast function sends a message to all connected clients except the sender. The receive function accepts incoming client connections and adds them to the clients and nicknames lists. It then sends a welcome message to the client and starts a new thread to handle the client's messages.

The handle function receives messages from a client and broadcasts them to all other connected clients. If an exception is raised, the client is removed from the clients and nicknames lists, and the thread is terminated.

## Client
The client file client.py connects to the server on localhost and port 9090 using the socket module. It then prompts the user to enter a nickname for the chat session using the tkinter.simpledialog.askstring method.

The client uses the threading module to create two threads: one to run the GUI and another to handle incoming messages. The gui_loop function creates a tkinter window with a chat area, message input area, and send button. The write function sends a message to the server when the send button is clicked.

The stop function stops the client from running and closes the GUI window. The receive function runs continuously and receives messages from the server. If the received message is the "NICK" message from the server, the client sends its nickname to the server. Otherwise, the message is displayed in the chat area.

Note that this chat application uses a simple protocol where messages are sent as strings of bytes encoded in UTF-8. There is no encryption or authentication, so it is not secure for transmitting sensitive information.
