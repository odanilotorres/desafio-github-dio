import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket criado com sucesso !!')

host = 'localhost'
porta = 5433

msg = 'Olá Servidor, tudo bem ?'

try:
    print('Cliente: ' + msg)
    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4069)

    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechando a conexão.')
    s.close()