from datetime import datetime
from queue import Queue
from configuration import configuration
from connectionlog import ConnectionLog

class Logger:
    def __init__(self,_ip_address,_enabled):
        self._separator = ";"
        self._enabled = _enabled
        self._ip_address = _ip_address
        if _enabled == False:
            return
        self._created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self._filename = self._ip_address + "_" + str(self._created_at)+".log"
        self._file = open("./logs/"+self._filename,"w")
        pass

    def write_log(self,_title,_content) -> bool:
        _at = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        _content = _title + self._separator + _content
        _data_to_write = _at + self._separator + _content+"\r\n"
        configuration.send_message({"type":"send_log","data":ConnectionLog(self._ip_address,_at,_content)})
        if self._enabled == False:
            return True
        self._file.write(_data_to_write)
        return True

    def close_log(self) -> bool:
        if self._enabled == False:
            return True
        self._file.close()
        return True
