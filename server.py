import socket
import json
import ast
import time
server_sock=socket.socket()
print("Socket is created")
port=1055
localhost=socket.gethostbyname(socket.gethostname())
server_sock.bind((localhost,port))
print("socket bined to port no: ",port)
server_sock.listen(5)
print("socket is listening")
dict1={"name":"gokul","place":"Neyyatinkara"}
k=json.dumps(dict1)
def allocate_bu(dat):
    b_units=['TRA','EMB','MED','MEG','ICP','DPS']
    o=dat["branch"]
    if o=="EC":
      BU='EMB'
    elif o=="ME":
      BU='TRA'
    elif o=="EE":
      BU='MEG'
    elif o=="CS":
      BU='ICP'
    
    else:
      BU='MED'
    name=dat["name"]

    k=f"Hi {name}, your BU is {BU}"
    return k


client_soc,address=server_sock.accept()
print("connected to address",address)
dat=client_soc.recv(1000)
dat=dat.decode("utf-8")
dat = ast.literal_eval(dat)
print("Student name : ",dat["name"])
print("College name : ",dat["college"])
print("Branch Name : ",dat["branch"])
out=allocate_bu(dat)
client_soc.send(bytes(out,'utf-8'))
time.sleep(5)
client_soc.close()

