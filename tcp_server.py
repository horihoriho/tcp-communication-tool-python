# -*- coding: utf-8 -*-
import socket
import logging
import errno

# Server connection settings
SERVER_IP = "127.0.0.1" 
SERVER_PORT = 8080

# The maximum number of queued connections
LISTEN_NUM = 5

# The maximum size of data received from the client at one time
BUFFER_SIZE = 1024


# Configure basic logging settings
logging.basicConfig(
    filename="./logs/server.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def start_server():
    """
    Start a TCP server, receive messages from clients, and send responses. 
    """
    try:
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
                    try:
                        # Receive data from the client as bytes
                        data = client.recv(BUFFER_SIZE)

                        # Check whether the client sent any data
                        if not data:
                            print("Client disconnected without sending data.")
                            logging.warning(f"Client disconnected without sending data: {address}")
                            continue

                        # Decode bytes into a UTF-8 string
                        message = data.decode("utf-8")

                        # Treat empty or whitespace-only messages as invalid
                        if message.strip() == "":
                            print("Empty message received.")
                            logging.warning(f"Empty message received from {address}")
                            continue

                        print(f"Received: {message}")
                        logging.info(f"Message received from {address}: {message}")

                        response = f"Received: {message}"

                        # Encode the response string into bytes and send it back
                        client.sendall(response.encode("utf-8"))
                        logging.info(f"Response sent to {address}: {response}")
                    
                    except UnicodeDecodeError:
                        print("Failed to decode received data.")
                        logging.error(f"Failed to decode received data from {address}")

                    except BrokenPipeError:
                        print("Client disconnected before the response could be sent.")
                        logging.error(f"Client disconnected before the response could be sent: {address}")

                    except ConnectionResetError:
                        print("Connection reset by client.")
                        logging.error(f"Connection reset by client: {address}")

                    except OSError as e:
                        print("Socket error occurred during client communication.")
                        logging.error(f"Socket error occurred during client communication with {address}: {e}")

                    # Always record connection closure, whether communication succeeds or fails
                    finally:
                        logging.info(f"Connection closed: {address}")


    except OverflowError:
        print("Server start failed: port number must be 0-65535.")
        logging.error("Server start failed: port number must be 0-65535")

    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print("Server start failed: address already in use.")
            logging.error("Server start failed: address already in use")
        else:
            print("Socket error occurred. Please check the server settings.")
            logging.error(f"Socket error occurred: {e}") 

    except Exception:
        print("Unexpected error occurred.")
        logging.exception("Unexpected error occurred")
        


if __name__ == "__main__":
    start_server()


