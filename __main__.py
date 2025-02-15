import json
import selectors
import socket
import time
from configuration import Configuration
from connection import Connection
from filestructure import FileStructure
file = open("./config.json")
config = json.loads(file.read())
file.close()
configuration = Configuration(config["server_type"],config["data_port"],config["command_port"],config["filesystem_depth"],config["file_ratio"],config["directory_ratio"],config["average_entity_per_directory"],config["logging"],config["allowed_users"])
selector = selectors.DefaultSelector()

def accept_connection(server_sock):
    """Accept a new connection and create a Connection object."""
    conn, addr = server_sock.accept()
    print(f"Accepted connection from {addr}")
    connection = Connection(conn, addr[0], selector,configuration,configuration.get_logging())
    if not selector.get_map().get(conn.fileno()):  
        selector.register(conn, selectors.EVENT_READ, connection.handle_connection)

def start_server(host='127.0.0.1', port=config["command_port"]):
    """Start the non-blocking server."""
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
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
        server_sock.close()
        selector.close()

def create_server_structure():
    f = FileStructure(configuration.get_filesystem_depth(),configuration.get_file_ratio(),configuration.get_directory_ratio(),configuration.get_average_entity_per_directory())
    f.generate_directory_structure()
    pass

if __name__ == "__main__":
    #create_server_structure()
    start_server()
    pass
