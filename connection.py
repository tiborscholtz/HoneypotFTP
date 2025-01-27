from datetime import datetime
from math import floor
import selectors
import socket

from command import Command
from configuration import Configuration
from logger import Logger

class Connection:

    def __init__(self,_connection,_ip_address,_selector,_configuration:Configuration,_logging):
        self._selector = _selector
        self._connection = _connection
        self._ip_address = _ip_address
        self._logger = Logger(self._ip_address,_logging)
        self._configuration = _configuration
        self._connected_at = datetime.now()
        self._connection.setblocking(False)
        self._selector.register(self._connection, selectors.EVENT_READ, self.handle_connection)
        self._data_socket = None
        self._data_port = None
        pass

    def _setup_data_socket(self) -> dict:
        self._data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._data_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
        self._data_socket.bind(('', 0))
        self._data_socket.listen(100)
        self._data_socket.setblocking(False)  # Set
        self._selector.register(self._data_socket, selectors.EVENT_READ, self.handle_data_connection)
        self._data_port = self._data_socket.getsockname()[1]
        ports = {"first":0,"second":0}
        first_port = floor(self._data_port / 256)
        second_port = (self._data_port) - (first_port * 256)
        ports["first"] = first_port
        ports["second"] = second_port
        return ports

    def _get_command_response(self,_command:Command) -> list:
        _response = []
        if _command.is_command("USER"):
            self._logger.write_log("USER","Username: " + _command.get_parameter_at_index(0) + " login request.")
            _response = _command.get_response({"username":_command.get_parameter_at_index(0)})
            pass
        if _command.is_command("PASS"):
            self._logger.write_log("PASS","Password: " + _command.get_parameter_at_index(0) + " login request.")
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("PWD"):
            self._logger.write_log("PWD","Print working directory requested. Current directory is: /.")
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("CWD"):
            self._logger.write_log("PWD","Change working directory requested. Current directory is: /.")
            _response = _command.get_response({"directory":"/"})
            pass
        if _command.is_command("PASV"):
            self._logger.write_log("PWD","Passive mode requested.")
            _ports = self._setup_data_socket()
            _response = _command.get_response({"ip1":"0","ip2":"0","ip3":"0","ip4":"0","port1":_ports["first"],"port2":_ports["second"]})
            pass
        if _command.is_command("TYPE") and _command.get_parameters_length() == 1:
            if _command.get_parameter_at_index(0) == "A":
                self._logger.write_log("TYPE","ASCII type requested.")
                _response = _command.get_response({"type":"ASCII"})
            elif _command.get_parameter_at_index(0) == "I":
                self._logger.write_log("TYPE","8 bit binary type requested.")
                _response = _command.get_response({"type":"I"})
            else:
                self._logger.write_log("TYPE","ASCII type requested.")
                _response = _command.get_response({"type":"ASCII"})
            pass
        if _command.is_command("LIST"):
            self._logger.write_log("LIST","Listing files requested.")
            _response = _command.get_response({"type":"ASCII"})
            pass
        if _command.is_command("QUIT"):
            self._logger.write_log("QUIT","Quit requested.")
            _response = _command.get_response({"downloaded":"0","uploaded":"0"})
            pass
        return _response
    
    def handle_connection(self,_connection):
        """Handle ftp communication with a client."""
        try:
            data = _connection.recv(1024)  # Read data from the client
            if data:
                command = Command(data)
                print(command)
                _response = self._get_command_response(command)
                print("_response is")
                print(_response)
                for to_send in _response:
                    _connection.sendall(bytes(to_send["content"]+"\r\n",encoding="utf-8"))  # Echo the data back to the client
            else:
                print("Client closed the connection")
                self._selector.unregister(self._connection)  # Unregister the connection
                self._connection.close()
        except ConnectionResetError:
            print("Connection reset by client")
            self._selector.unregister(self._connection)
            self._connection.close()

    def handle_data_connection(self,_connection):
        """Handle ftp communication with a client."""
        try:
            data = _connection.recv(1024)  # Read data from the client
            if data:
                command = Command(data)
                print(command)
                _response = self._get_command_response(command)
                print("_response is")
                print(_response)
                for to_send in _response:
                    _connection.sendall(bytes(to_send["content"]+"\r\n",encoding="utf-8"))  # Echo the data back to the client
            else:
                print("Client closed the connection")
                self._selector.unregister(self._connection)  # Unregister the connection
                self._connection.close()
        except ConnectionResetError:
            print("Connection reset by client")
            self._selector.unregister(self._data_socket)
            self._data_socket.close()
