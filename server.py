import socket
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',9090))
server.listen()
#client,addr=server.accept()

clients=[]
nicknames=[]

##broadcast
def broadcast(msg):
    #msg is str
    for client in clients:
        client.send(msg)


##receive
def receive():
    while True:
        #print('recieve loop')
        client,addr=server.accept()
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} is connected to server.\n".encode('utf-8'))
        client.send("%m Connected to server".encode('utf-8'))
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

##handle
def handle(client):
    while True:
        #print('handle loop')
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except Exception as e:
            print(f'handle exception : {str(e)}')
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break

receive()