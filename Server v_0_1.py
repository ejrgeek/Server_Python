import socket
from os import system
ip = '0.0.0.0'
port = 669
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server.bind((ip,port))
	server.listen(5)

	print('Maquina >',ip,port)
	(obj, cliente) = server.accept()
	print("Maquinas Conectadas > ",cliente[0])
	
	while True:
		msg = obj.recv(1024)
		msg = msg[:-1]
		print(cliente[0],">",msg)
		if msg == "ls":
			system('ls')
		elif msg == 'ifconfig':
			system('ifconfig')
		elif msg == 'exit':
			server.close()

	server.close()
except Exception as erro:
	print(erro)
	server.close()
