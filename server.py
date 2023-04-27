import socket

serverSocket = socket.socket()
print("Socket has been created")
serverSocket.bind(("localhost", 1084))
serverSocket.listen(3)
print("Waiting for connection")
while True:
    c, addr = serverSocket.accept()
    name = c.recv(1024).decode()
    print(f"{name } connected with {addr}")

    c.send(bytes("Welcome to Amir's Server","utf-8"))
    c.close()

