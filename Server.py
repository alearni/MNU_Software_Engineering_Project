import socket
import threading

def handle_client(client_socket):
    # Send welcome message
    client_socket.send("Welcome to the server!\n".encode())
    
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Decode and print received message
            received_message = data.decode()
            print("[*] Received from client {}: {}".format(client_socket.getpeername(), received_message))
            
            # Check if client wants to close the connection
            if received_message.strip().lower() == "close":
                print("[*] Client requested to close the connection.")
                break
            
            # Prompt server to enter a message to send to the client
            message_to_send = input("Enter message to send to client: ")
            # Send the message to the client
            client_socket.send(message_to_send.encode())
        except Exception as e:
            print("Error:", str(e))
            break
    
    # Close client connection
    client_socket.close()

def main():
    # Server configuration
    host = "127.0.0.1"
    port = 7505

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("[*] Listening on {}:{}".format(host, port))

    while True:
        # Accept incoming connection from client
        client_socket, addr = server_socket.accept()
        print("[*] Accepted connection from: {}:{}".format(addr[0], addr[1]))

        # Handle client connection in a new thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
