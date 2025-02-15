class ConnectionLog:
    def __init__(self,_ip_address,_timestamp,_text):
        self._ip_address = _ip_address
        self._timestamp = _timestamp
        self._text = _text
        pass

    def get_ip_address(self):
        return self._ip_address
    
    def get_timestamp(self):
        return self._timestamp
    
    def get_text(self):
        return self._text