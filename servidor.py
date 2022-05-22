import socket

HOST = 'localhost'
PORT = 5555
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print('Aguardando conexao')
cliente, end = servidor.accept()
print('conectado em', end)
while True:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        print('fechando conexao')
        cliente.close()
        break
    else:
        print(f'{msg}')
    cliente.send(str(input(f'mensagem: ')).encode('utf-8'))
servidor.close()
