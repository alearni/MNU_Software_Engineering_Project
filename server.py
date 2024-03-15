# from socket import *

# try:
#     s=socket(AF_INET, SOCK_STREAM)
#     host="127.0.0.1"
#     port=7002
#     s.bind((host,port))
#     s.listen(5)
    
#     client ,addr=s.accept()
    
#     print("connection from: " ,addr[0])
    
#     while True:
        
#         x=client.recv(2048)
#         print("client: ", x.decode('utf-8'))
        
#         y=input("server: ")
#         client.send(y.encode("utf-8"))
#     s.close()
    
# except error as e:
#     print(e)
# except KeyboardInterrupt:
#     print("Chat terminated")        

import socket
import threading

HOST = "127.0.0.1"
PORT = 7002

def handle_client(client_socket, address):
  print(f"Connection from: {address[0]}")
  while True:
    try:
      data = client_socket.recv(2048).decode("utf-8")
      if not data:
        break
      print(f"client: {data}")
      server_message = input("server: ")
      client_socket.send(server_message.encode("utf-8"))
    except (ConnectionError, ConnectionAbortedError):
      print(f"Client {address[0]} disconnected")
      break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind((HOST, PORT))
  server_socket.listen(5)
  print(f"Server listening on {HOST}:{PORT}")
  while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()

print("Server shutting down")
