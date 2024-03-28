from socket import *
import threading

s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen()
#client,add = s.accept()

# while True:
    
#     y=client.recv(2048)
#     print("client:",y.decode("utf-8"))
    
#     x=input("server: ")
#     client.send(x.encode("utf-8"))
# s.close()

def send_message(s):
    while True:
        y=input("server:")
        s.send(y.encode("utf-8"))
        
def recv_message(s):
    while True:
        x=s.recv(2048)
        print("client:",x.decode("utf-8"))
while True:
    client,add=s.accept()
    
    t1 = threading.Thread(target=send_message , args=(client,))
    t2=threading.Thread(target=recv_message, args=(client,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()