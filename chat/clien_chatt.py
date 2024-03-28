from socket import *
import threading

s= socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",1234))

# while True:
#     y=input("client:")
#     s.send(y.encode("utf-8"))
    
#     x=s.recv(2048)
#     print("server:",x.decode("utf-8"))
# s.close()

def send_message(s):
    while True:
        y=input("clien:")
        s.send(y.encode("utf-8"))
        
def recv_message(s):
    while True:
        x=s.recv(2048)
        print("server:",x.decode("utf-8"))
        

t1 = threading.Thread(target=send_message , args=(s,))
t2=threading.Thread(target=recv_message, args=(s,))
    
t1.start()
t2.start()
    
t1.join()
t2.join()
