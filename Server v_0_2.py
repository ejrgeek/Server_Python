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
	print("Maquina Conectada > ",cliente[0])
	
	while True:
		msg = obj.recv(1024)
		msg = msg[:-1]
		print(cliente[0],">",msg)
		if msg == "ls":
			system('ls')
		
		elif msg == 'ifconfig':
			system('ifconfig')
		
		elif msg == 'whoami':
			system('whoami')
		
		elif msg == 'cd':
			system('cd')
			
		elif msg == 'cp':
			system('cp')
			
		elif msg == 'rm':
			system('rm')
		
		elif msg == 'cat':
			system('cat')
			
		elif msg == 'ssh':
			system('ssh')
		
		elif msg == 'scp':
			system('scp')
		
		elif msg == 'chmod':
			system('chmod')
		
		elif msg == 'passwd':
			system('passwd')
			
		
		elif msg == 'mv':
			system('mv')
			
			
		elif msg == 'exit':
			server.close()
		else:
			print("Comando não Encontrado")
except Exception as erro:
	print(erro)
	server.close()
