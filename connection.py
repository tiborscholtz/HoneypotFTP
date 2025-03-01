from datetime import datetime
import json
from math import floor
import selectors
import socket

from command import Command
from configuration import Configuration
from logger import Logger

class Connection:

    def __init__(self,_id,_connection,_ip_address,_selector,_configuration:Configuration,_logging):
        self._id = _id
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
        self._client_socket = None
        command = Command(b'WELCOME')
        _response = self._get_command_response(command)
        self.send_responses(_response)
        pass


    def get_id(self):
        return self._id
    
    def get_ip_address(self):
        return self._ip_address
    
    def get_connected_at(self):
        return self._connected_at

    def _setup_data_socket(self,port_n = 0) -> dict:
        print("port_n")
        print(port_n)
        if self._data_socket:
            try:
                print("HERE")
                self._selector.unregister(self._data_socket)
            except KeyError as e:
                print(e)
                print("ERROR")
                # The socket was not registered, no need to unregister
                pass
            finally:
                print("_data_socket finally")
                print(self._data_socket)
                self._data_socket.close()
                self._data_socket = None
                self._data_port = None
        print(self._data_socket)
        print(self._data_port)
        self._data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._data_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
        print(self._data_socket)
        self._data_socket.bind(('', 0))
        self._data_socket.listen(10)
        self._data_socket.setblocking(False)  # Set
        self._data_port = self._data_socket.getsockname()[1]
        ports = {"first":0,"second":0}
        first_port = floor(self._data_port / 256)
        second_port = (self._data_port) - (first_port * 256)
        ports["first"] = first_port
        ports["second"] = second_port
        return ports

    def _get_command_response(self,_command:Command) -> list:
        _response = []
        if _command.is_command("WELCOME"):
            _response = _command.get_response({"current":1,"allowed_users":50,"time":datetime.today().strftime('%Y-%m-%d %H:%M:%S'),"port":self._configuration.get_command_port()})
            pass
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
        if _command.is_command("PORT") and _command.get_parameters_length() == 1:
            self._logger.write_log("PORT","PORT requested from client.")
            sent_data = _command.get_parameter_at_index(0).split(',')
            data_p = (int(sent_data[4]) * 256) + int(sent_data[5])
            _ports = self._setup_data_socket(data_p)
            ip = socket.gethostbyname(socket.gethostname())
            _response = _command.get_response({})
            pass
        if _command.is_command("PASV"):
            self._logger.write_log("PWD","Passive mode requested.")
            _ports = self._setup_data_socket(0)
            ip = socket.gethostbyname(socket.gethostname())
            _response = _command.get_response({"ip1":ip.split('.')[0],"ip2":ip.split('.')[1],"ip3":ip.split('.')[2],"ip4":ip.split('.')[3],"port1":_ports["first"],"port2":_ports["second"]})
            pass
        if _command.is_command("EPSV"):
            self._logger.write_log("EPSV","Extended Passive mode requested.")
            _ports = self._setup_data_socket()
            _response = _command.get_response({"port":self._data_port})
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
            entries = [
                "drwxrwxr-x  6 tibor tibor   4096 Feb 15 20:23 .",
                "drwxrwxr-x 19 tibor tibor   4096 Feb 23 20:12 ..",
                "-rw-rw-r--  1 tibor tibor   1548 Feb 15 10:41 command.py",
                "-rw-rw-r--  1 tibor tibor    236 Feb 15 16:37 config.json",
                "-rw-rw-r--  1 tibor tibor   2806 Feb 15 20:35 configuration.py",
                "-rw-rw-r--  1 tibor tibor    372 Feb 15 20:25 connectionlog.py",
                "-rw-rw-r--  1 tibor tibor   7368 Feb 28 20:04 connection.py",
                "-rw-rw-r--  1 tibor tibor   4837 Feb 15 20:20 constants.py",
                "-rw-rw-r--  1 tibor tibor    252 Feb 14 17:26 default_config.py",
                "-rw-rw-r--  1 tibor tibor    566 Feb 14 18:54 entityFile.py",
                "-rw-rw-r--  1 tibor tibor    485 Feb 15 17:13 entityFolder.py",
                "-rw-rw-r--  1 tibor tibor   3145 Feb 13 22:27 entity.py",
                "drwxrwxr-x  5 tibor tibor   4096 Jan 22 19:45 env",
                "-rw-rw-r--  1 tibor tibor   1702 Feb 14 19:04 filestructure.py",
                "-rw-r--r--  1 tibor tibor 252816 Dec 31 23:36 ftp_test.pcapng",
                "drwxrwxr-x  8 tibor tibor   4096 Feb 15 21:05 .git",
                "-rw-rw-r--  1 tibor tibor   3415 Jan 22 19:44 .gitignore",
                "-rw-rw-r--  1 tibor tibor   1069 Jan 22 19:44 LICENSE",
                "-rw-rw-r--  1 tibor tibor   1121 Feb 15 20:55 logger.py",
                "drwxrwxr-x  2 tibor tibor   4096 Feb 15 16:37 logs",
                "-rw-rw-r--  1 tibor tibor   6798 Feb 28 18:45 __main__.py",
                "drwxrwxr-x  2 tibor tibor   4096 Feb 28 20:04 __pycache__",
                "-rw-rw-r--  1 tibor tibor   2983 Jan 22 20:45 README.md",
                "-rw-rw-r--  1 tibor tibor   3282 Feb 28 20:03 responses.py",
                "-rw-rw-r--  1 tibor tibor   2453 Feb 15 17:15 screen.py"
            ]

            ftp_list_response = "\r\n".join(entries)
            self._logger.write_log("LIST","Listing files requested.")
            _response = _command.get_response({"data":ftp_list_response,"totalmatches":len(entries)})
            pass
        if _command.is_command("QUIT"):
            self._logger.write_log("QUIT","Quit requested.")
            _response = _command.get_response({"downloaded":"0","uploaded":"0"})
            pass
        return _response
    
    def send_responses(self,_responses):
        for to_send in _responses:
            if to_send["type"] == "plain":
                try:
                    self._connection.sendall(bytes(to_send["content"]+"\r\n",encoding="utf-8"))  # Echo the data back to the client
                    pass
                except Exception:
                    pass
            if to_send["type"] == "data":
                self._selector.register(self._data_socket, selectors.EVENT_READ, lambda sock: self._send_data(sock,bytes(to_send["content"]+ "\r\n",encoding="utf-8")))
        return True

    def handle_connection(self,_connection):
        """Handle ftp communication with a client."""
        try:
            data = _connection.recv(1024)  # Read data from the client
            if data:
                print(data)
                command = Command(data)
                _response = self._get_command_response(command)
                self.send_responses(_response)
            else:
                self._selector.unregister(self._connection)  # Unregister the connection
                self._connection.close()
                self._logger.close_log()
        except ConnectionResetError:
            self._selector.unregister(self._connection)
            self._connection.close()
            self._logger.close_log()

    def _send_data(self, data_socket,_data):
        data_conn, _ = data_socket.accept()
        data_conn.sendall(_data)
        data_conn.close()
        self._selector.unregister(self._data_socket)
        self._data_socket.close()
        self._data_socket = None
        self._data_port = None

    def read_data(self, client_socket):
        """Handle reading from a data connection."""
        try:
            data = client_socket.recv(1024)
            if data:
                command = Command(data)
            else:
                self._selector.unregister(client_socket)
                client_socket.close()
        except BlockingIOError:
            # No data available yet; retry later
            pass  


