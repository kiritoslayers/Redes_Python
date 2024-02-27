#!/user/bin/python3
import socket


# referese a um socket tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# criando a conexão
server.connect(('localhost', 9473))

# criando loop infinito
while True:
    msg = input('Digite aqui a sua mensagem: ')
    # envia a mensagem
    server.send(msg.encode())