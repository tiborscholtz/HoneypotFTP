import json
import selectors
import socket
import time
from configuration import Configuration
from connection import Connection
file = open("./config.json")
config = json.loads(file.read())
file.close()
configuration = Configuration(config["server_type"],config["data_port"],config["command_port"],config["filesystem_depth"],config["file_ratio"],config["directory_ratio"],config["average_file_per_directory"])
print(config["data_port"])
selector = selectors.DefaultSelector()

selector = selectors.DefaultSelector()

def accept_connection(server_sock):
    """Accept a new connection and create a Connection object."""
    conn, addr = server_sock.accept()
    print(f"Accepted connection from {addr}")
    connection = Connection(conn, addr, selector,configuration)
    selector.register(conn, selectors.EVENT_READ, connection.handle_read)

def start_server(host='127.0.0.1', port=config["data_port"]):
    """Start the non-blocking server."""
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(100)
    server_sock.setblocking(False)  # Set the server socket to non-blocking mode
    print(f"Server started on {host}:{port}")
    selector.register(server_sock, selectors.EVENT_READ, accept_connection)
    try:
        while True:
            events = selector.select(timeout=None)  # Wait for events
            for key, _ in events:
                callback = key.data  # Retrieve the callback function
                callback(key.fileobj)  # Call the callback with the socket
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        selector.close()

if __name__ == "__main__":
    start_server()
