import socket
PORT=12345
SERVER=socket.gethostbyname(socket.gethostname())
ADDRESS=(SERVER,PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="quit"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDRESS)
server.listen()
print("server is active...\n")


client_socket, client_address =server.accept()
client_socket.send("connection established".encode(FORMAT))

while True:
    message=client_socket.recv(BYTESIZE).decode(FORMAT)
    if message==DISCONNECT_MESSAGE:
        client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))
        print("client exited...\n")
        break
    else:
        print(f"{message}\n")
        message=input("message: ")
        client_socket.send(message.encode(FORMAT))

client_socket.close()