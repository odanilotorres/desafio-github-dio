import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criada com sucesso!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
msg = '\nServidor: Olá Cliente, tudo certo com você ?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (msg.encode()), end)

