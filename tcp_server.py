# -*- coding : UTF-8 -*-
import socket
import logging

# client connection settings
SERVER_IP = "127.0.0.1" 
SERVER_PORT = 8080

# The maximum number of queued connections
LISTEN_NUM = 5

# The maximum size of data received from the client at once time
BUFFER_SIZE = 1024


# Configure basic logging settings
logging.basicConfig(filename="/logs/server.log", level=logging.INFO, format="%(levelname)s: %(message)s")


def start_server():
    """
    Start a TCP server, receive message from clients, and send responses. 
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:
        # Bind the server socket to server IP address and port
        tcp_server.bind((SERVER_IP, SERVER_PORT))
        # Start listening for incoming client connections
        tcp_server.listen(LISTEN_NUM)
        print(f"Server started on {SERVER_IP}:{SERVER_PORT}")
        logging.info(f"Server started on {SERVER_IP}:{SERVER_PORT}")

        while True:
            # Wait for a client connection
            client, address = tcp_server.accept()
            logging.info(f"Client connected: {address}")

            # Automatically close the client socket after communication
            with client:
                # Recieved data from the client as bytes
                data = client.recv(BUFFER_SIZE)

                # Decode bytes into a UTF-8 string
                message = data.decode("utf-8")
                print(f"Received: {message}")
                logging.info(f"Message received: {message}")

                response = f"Received: {message}"

                # Encode strings into bytes and send it back
                client.sendall(response.encode("utf-8"))
                logging.info(f"Response sent: {response}")

                logging.info(f"Connection closed: {address}")

if __name__ == "__main__":
    start_server()


