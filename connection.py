from datetime import datetime
from math import floor
import selectors

from command import Command
from configuration import Configuration

class Connection:

    def __init__(self,_connection,_ip_address,_selector,_configuration:Configuration):
        self._selector = _selector
        self._connection = _connection
        self._ip_address = _ip_address
        self._configuration = _configuration
        self._connected_at = datetime.now()
        self._connection.setblocking(False)
        self._selector.register(self._connection, selectors.EVENT_READ, self.handle_connection)
        pass


    def _get_response(_command:Command) -> list:
        _response = []
        if _command.is_command("USER"):
            _response = _command.get_response({"username":_command.get_parameter_at_index(0)})
            pass
        if _command.is_command("PASS"):
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("PWD"):
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("CWD"):
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("PASV"):
            _response = _command.get_response({"ip1":"0","ip2":"0","ip3":"0","ip4":"0","port1":"0","port1":"0"})
            pass
        if _command.is_command("TYPE") and _command.get_parameters_length() == 1:
            if _command.get_parameter_at_index(0) == "A":
                _response = _command.get_response({"type":"ASCII"})
            else:
                _response = _command.get_response({"type":"ASCII"})
            pass
        if _command.is_command("LIST"):
            _response = _command.get_response({"type":"ASCII"})
            pass
        if _command.is_command("QUIT"):
            _response = _command.get_response({"downloaded":"0","uploaded":"0"})
            pass
        return _response
    def handle_connection(self,_connection):
        """Handle communication with a client."""
        try:
            data = _connection.recv(1024)  # Read data from the client
            if data:
                command = Command(data)
                print(f"Received data: {data.decode('utf-8')}")
                _response = self._get_response(command)
                _connection.sendall(b"Echo: " + data)  # Echo the data back to the client
            else:
                print("Client closed the connection")
                self._selector.unregister(self._connection)  # Unregister the connection
                self._connection.close()
        except ConnectionResetError:
            print("Connection reset by client")
            self._selector.unregister(self._connection)
            self._connection.close()
