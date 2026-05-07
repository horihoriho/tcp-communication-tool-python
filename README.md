# tcp-communication-tool-python

This is a simple TCP client-server communication tool built with Python.
The purpose of this project is to understand basic TCP/IP communication, event logging, and error handling in socket programming.

## Features

- TCP client-server communication
- Message sending and receiving
- Event logging for both client and server
- Client-side error handling
- Server-side error handling
- Timeout handling
- Input validation for empty messages
- Socket resource management using `with` statements

## Technologies Used

- Python
- socket
- logging
- errno

## Project Structure

```text
tcp-communication-tool-python/
|--- tcp_client.py
|--- tcp_server.py
|--- logs/
|   |--- client.log
|   |--- server.log
|--- README.md
```

## How to Run

Coming soon.

## Test Cases

| Case | Expected Result | Status |
|---|---|---|
| Normal communication | Client receives a response from the server | Passed |
| Server is not running | Client shows a connection failure message | Passed |
| Wrong client port | Client shows a connection failure message | Passed |
| Invalid client IP | Client shows a socket error message | Passed |
| Client timeout | Client shows a timeout message | Passed |
| Empty client message | Client does not send the message | Passed |
| Server port already in use | Server shows an address-in-use message | Passed |
| Invalid server port | Server shows a port range error message | Passed |
| Invalid server IP | Server shows a socket error message | Passed |
| Client disconnects without sending data | Server logs a warning | Passed |

## Error Handling

This project includes basic error handling for both the client and the server.

### Client-side error handling

- `ConnectionRefusedError`
- `TimeoutError`
- `OSError`
- Unexpected errors

### Server-side error handling 

- Port already in use
- Invalid port number
- Invalid server IP address
- Empty received data
- Empty message
- `UnicodeDecodeError`
- `BrokenPipeError`
- `ConnectionResetError`
- `OSError`
- Unexpected errors

## What I Learned

Through this project, I learned:

- How TCP client-server communication works
- How to use Python's `socket` module
- How to record communication events using the `logging` module
- How to handle common socket errors
- How to use `with` statements for safe socket resource management
- How to design communication software that is easy to debug

## Future Improvements
- Support multiple clients
- Add command-line arguments for IP address and port number
- Add log rotation
- Add unit tests
- Support configuration files
- Add TLS/SSL communication 


