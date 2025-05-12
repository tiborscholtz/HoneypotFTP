import codecs
from datetime import datetime
from queue import Queue
from configuration import configuration
from connectionlog import ConnectionLog
import json

class Logger:
    def __init__(self,_ip_address,_enabled,_extended_log_on_disconnect):
        self._extended_log_on_disconnect = _extended_log_on_disconnect
        self._separator = ";"
        self._enabled = _enabled
        self._ip_address = _ip_address
        if _enabled == False:
            return
        self._created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self._filename = "./logs/"+self._ip_address + "_" + str(self._created_at)
        self._extension = ".log"
        self._file = open(self._filename+self._extension,"w")
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
        if self._extended_log_on_disconnect:
            with open(self._filename+self._extension, 'r') as file:
                json_data = []
                lines = file.readlines()
                for i in range(len(lines)):
                    one_line = lines[i].strip("\n").split(self._separator)
                    one_data = {}
                    one_data["time"] = one_line[0]
                    one_data["command"] = one_line[1]
                    one_data["data"] = one_line[2]
                    json_data.append(one_data)
                with open(self._filename+".json", 'w') as f:
                    json.dump(json_data, f,ensure_ascii=False)
            pass
        return True
