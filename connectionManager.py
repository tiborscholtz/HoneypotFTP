import threading


class ConnectionManager:
    def __init__(self):
        self.connections = []
        self.lock = threading.Lock()

    def add_connection(self, connection):
        with self.lock:
            self.connections.append(connection)

    def remove_connection(self, conn_id):
        with self.lock:
            self.connections = [conn for conn in self.connections if conn.get_id() != conn_id]

    def get_all_connections(self):
        with self.lock:
            return list(self.connections)
   
    def get_all_connections_length(self):
        with self.lock:
            return len(list(self.connections))