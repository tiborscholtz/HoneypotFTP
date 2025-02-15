from datetime import datetime


class Logger:
    def __init__(self,_ip_address,_enabled):
        self._enabled = _enabled
        if _enabled == False:
            return
        self._ip_address = _ip_address
        self._created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self._filename = self._ip_address + "_" + str(self._created_at)+".log"
        self._file = open("./logs/"+self._filename,"w")
        pass

    def write_log(self,_title,_content) -> bool:
        if self._enabled == False:
            return True
        _at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        _data_to_write = str(_at) + " - " + _title + " - " + _content+"\r\n"
        self._file.write(_data_to_write)
        return True

    def close_log(self) -> bool:
        if self._enabled == False:
            return True
        self._file.close()
        return True
