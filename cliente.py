import socket

HOST = 'localhost'
PORT = 5555
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print('digite tt para terminar o chat')
while True:
    cliente.send(str(input(f'mensagem: ')).encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        break
    else:
        print(f'{msg}')
cliente.close()
