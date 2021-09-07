import socket
import json
import pandas as pd

import time
details={}
k=input("Enter employee name : ")
details["name"]=k
l=input("Enter college name : ")
details["college"]=l
n=input("Enter application number : ")
details["app"]=n
b=input("Enter the branch (ME,EC,CS,EE,IE): ")
details["branch"]=b
dat=json.dumps(details)
client_socket=socket.socket()
print("socket created")
port=1055

localhost=socket.gethostbyname(socket.gethostname())
client_socket.connect((localhost,port))
print("connected")

client_socket.send(bytes(dat,'utf-8'))
time.sleep(3)
f=client_socket.recv(100)
f=f.decode("utf-8")
print(f)
client_socket.close()