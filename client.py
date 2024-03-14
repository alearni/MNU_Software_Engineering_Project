import socket

def main():
    # Server configuration
    host = "127.0.0.1"
    port = 7505

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive welcome message from server
    welcome_message = client_socket.recv(1024)
    print(welcome_message.decode())

    while True:
        # Input message from user
        message = input("Enter message (type 'close' to disconnect): ")

        # Send message to server
        client_socket.send(message.encode())

        # Check if user wants to close the connection
        if message.lower() == "close":
            break

        # Receive response from server
        response = client_socket.recv(1024)
        print("Server response:", response.decode())

    # Close client socket
    client_socket.close()

if __name__ == "__main__":
    main()
