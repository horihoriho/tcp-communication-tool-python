# -*- coding: utf-8 -*-
import socket
import logging

# Server connection settings
TARGET_IP = "127.0.0.1"
TARGET_PORT = 8080

# Maximum size of data received from the server at one time
BUFFER_SIZE = 4096

# Maximum time to wait for connection or response
TIMEOUT_SECONDS = 5

# Configure basic logging settings
logging.basicConfig(
    filename="./logs/client.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def send_message(message):
    """
    Send a message to the TCP server and print the response.
    
    Parameters
    ----------
    message : str
        The message to send to the TCP server.
    """
    logging.info("Client started") 

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
            tcp_client.settimeout(TIMEOUT_SECONDS)

            # Connect to the TCP server
            tcp_client.connect((TARGET_IP, TARGET_PORT))
            logging.info(f"Connected to server on {TARGET_IP}:{TARGET_PORT}") 
        
            # Send the message as UTF-8 encoded bytes
            tcp_client.sendall(message.encode("utf-8"))
            logging.info(f"Message sent: {message}") 
        
            # Receive the response from the server and decode it
            data = tcp_client.recv(BUFFER_SIZE)
            response = data.decode("utf-8")

            print(f"Response received: {response}")
            logging.info(f"Response received: {response}") 

            logging.info("Connection closed") 

    except ConnectionRefusedError:
        print("Connection failed: server is not running or the port number is incorrect.")
        logging.error("Connection failed: server is not running or the port number is incorrect.")

    except TimeoutError:
        print("Connection timed out: please check the IP address or network connection.")
        logging.error("Connection timed out: please check the IP address or network connection.")

    except OSError as e:
        print("Socket error occurred. Please check the IP address or connection settings.") 
        logging.error(f"Socket error occurred: {e}")

    except Exception:
        print("Unexpected error occurred.")
        logging.exception("Unexpected error occurred.")


if __name__ == "__main__":
    message = input("Enter message: ")
    send_message(message)
