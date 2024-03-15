# from socket import *

# try: 
#     s=socket(AF_INET, SOCK_STREAM)
#     host="127.0.0.1"
#     port=7002
#     s.connect((host, port))
#     while True:
#         y=input("client: ")
#         s.send(y.encode("utf-8"))
#         x=s.recv(2048)
#         print("server: ",x.decode("utf-8"))
#     s.close()
# except error as e :
#     print(e)
# except KeyboardInterrupt: 
#     print("chat is terminated")
















# # import threading
# # import socket

# # name=input("What's your name: ")

# # Client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # Client.connect(("127.0.0.1", 54322 ))

# # def receive():
# #     while True:
# #      try:
# #         message=Client.recv(1024).decode("ascii")
# #         if message =="nick":
# #             Client.send(name.encode("ascii"))
# #         else:
# #             print(message)
# #      except:
# #          print("an error occurred")
# #          Client.close()
# #          break

# # def write():
# #     while True:
# #       message=f"{name}=> {input("")} "
# #       Client.send(message.encode("ascii"))

# # receive_thread=threading.Thread(target=receive)
# # receive_thread.start()

# # write_thread=threading.Thread(target=write)
# # write_thread.start()


# import socket

# HOST = "127.0.0.1"  # Replace with server's IP address if connecting to a different machine
# PORT = 7002

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#   s.connect((HOST, PORT))
  
#   print(f"Connected to server at {HOST}:{PORT}")
  
#   while True:
#     # Send message to server
#     message = input("You: ")
#     s.sendall(message.encode("utf-8"))

#     # Receive message from server
#     data = s.recv(2048).decode("utf-8")
#     if not data:
#       break
#     print(f"Server: {data}")

# print("Connection closed")


# import socket
# import threading

# HOST = "127.0.0.1"
# PORT = 7002

# def handle_client(client_socket, address):
#   print(f"Connection from: {address[0]}")
#   while True:
#     try:
#       data = client_socket.recv(2048).decode("utf-8")
#       if not data:
#         break
#       print(f"client {address[0]}: {data}")
#       # Broadcast message to all connected clients (excluding sender)
#       for connected_client, _ in connections:
#         if connected_client != client_socket:
#           connected_client.sendall(f"Client {address[0]}: {data}".encode("utf-8"))
#     except (ConnectionError, ConnectionAbortedError):
#       print(f"Client {address[0]} disconnected")
#       connections.remove(client_socket)
#       break

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#   server_socket.bind((HOST, PORT))
#   server_socket.listen(5)
#   print(f"Server listening on {HOST}:{PORT}")
#   connections = []  # List to store connected client sockets
#   while True:
#     client_socket, address = server_socket.accept()
#     connections.append(client_socket)  # Add new connection to list
#     client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
#     client_thread.start()

# print("Server shutting down")
