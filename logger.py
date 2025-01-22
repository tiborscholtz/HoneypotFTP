from datetime import datetime


class Logger:
    def __init__(self,_ip_address):
        self._ip_address = _ip_address
        self._created_at = datetime.now()
        self._filename = self._ip_address + "_" + self._created_at+".log"
        self._file = open("./logs/"+self._filename)
        pass

    def write_log(self,_title,_content) -> bool:
        _at = datetime.now()
        _data_to_write = _at + " - " + _title + " - " + _content
        self._file.write(_data_to_write)
        return True

    def close_log(self) -> bool:
        self._file.close()
        return True
