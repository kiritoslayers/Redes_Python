#!/user/bin/python3
import socket


# referese a um socket tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# exemplo abaixo é referente a um socket UDP
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# escolhendo o ip e a porta da conexão
server.bind(('localhost', 9473))

# escutando a conexão'
server.listen()

# retorna o endereço de conexão 
coon, addr = server.accept()

# loop infinito para conexões
while True:
    # recebe a conexão
    data = coon.recv(1024)
    # valida se há dados, se caso não houver dados, ele para e aguarda até ter!
    if not data:
        break
    # transforma os bytes em string
    print(data.decode())

# fechando a conexão
coon.close()