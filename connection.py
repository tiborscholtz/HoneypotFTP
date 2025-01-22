from datetime import datetime

class Connection:

    def __init__(self,_ip_address,_command_connection):
        self._command_connection = _command_connection
        self._ip_address = _ip_address
        self._connected_at = datetime.now()
        pass