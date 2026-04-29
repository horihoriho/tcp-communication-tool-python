# -*- coding : UTF-8 -*-
import socket
import logging

# Server connection settings
TARGET_IP = "127.0.0.1"
TARGET_PORT = 8080

# Maximum size of data received from the server at once time
BUFFER_SIZE = 4096

# Configure basic logging settings
logging.basicConfig(filename="/logs/client.log", level=logging.INFO, format="%(levelname)s: %(message)s")


def send_message(message):
    """
    Send a message to the TCP server and print the response.
    
    Parameters
    ----------
    message : str
        The message to send to the TCP server.
    """
    logging.info(f"Client started") 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
        # Connect to the TCP server
        tcp_client.connect((TARGET_IP, TARGET_PORT))
        logging.info(f"Connected to server on {TARGET_IP}:{TARGET_PORT}") 
        
        # Send the message as UTF-8 encoded bytes
        tcp_client.sendall(message.encode("utf-8"))
        logging.info(f"Message sent: {message}") 
        
        # Receive the response from the server and decode it
        data = tcp_client.recv(BUFFER_SIZE)
        response = data.decode("utf-8")

        print(f"Received from server: {response}")
        logging.info(f"Received from server: {response}") 

        logging.info(f"Connection closed") 

if __name__ == "__main__":
    message = input("Enter message: ")
    send_message(message)
