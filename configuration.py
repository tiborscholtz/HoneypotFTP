import json
import queue
class Configuration:
    def __init__(self,_type,_command_port,_filesystem_depth,_file_ratio,_directory_ratio,_average_entity_per_directory,_logging,_allowed_users,_extended_log_on_disconnect,_modification_minutes_from,_modification_minutes_to,_different_structure_per_client,_file_byte_size_min,_file_byte_size_max):
        self._type = _type
        self._command_port = _command_port
        self._filesystem_depth = _filesystem_depth
        self._file_ratio = _file_ratio
        self._directory_ratio = _directory_ratio
        self._average_entity_per_directory = _average_entity_per_directory
        self._logging = _logging
        self._allowed_users = _allowed_users
        self._message_queue = queue.Queue()
        self._extended_log_on_disconnect = _extended_log_on_disconnect
        self._modification_minutes_from = _modification_minutes_from
        self._modification_minutes_to = _modification_minutes_to
        self._different_structure_per_client = _different_structure_per_client
        self._file_byte_size_min = _file_byte_size_min
        self._file_byte_size_max = _file_byte_size_max
        pass
    
    def send_message(self,_data):
        self._message_queue.put(_data)

    def get_message(self):
        return self._message_queue.get_nowait()

    def get_type(self):
        return self._type
    
    def get_command_port(self):
        return self._command_port
    
    def get_filesystem_depth(self):
        return self._filesystem_depth
    
    def get_file_ratio(self):
        return self._file_ratio
    
    def get_directory_ratio(self):
        return self._directory_ratio
    
    def get_logging(self):
        return self._logging
    
    def get_allowed_users(self):
        return self._logging
    
    def get_average_entity_per_directory(self):
        return self._average_entity_per_directory
    
    def get_extended_log_on_disconnect(self):
        return self._extended_log_on_disconnect

    def get_modification_minutes_from(self):
        return self._modification_minutes_from

    def get_modification_minutes_to(self):
        return self._modification_minutes_to
    
    def get_different_structure_per_client(self):
        return self._different_structure_per_client
    
    def get_file_byte_size_min(self):
        return self._file_byte_size_min

    def get_file_byte_size_max(self):
        return self._file_byte_size_max
    
    def get_object_format(self):
        return {
            "headers": ["Property", "Value","Description"],
            "data": [
                ["Type",self._type,"HoneyFTP can emulate several FTP server's response palette."],
                ["Command port", self._command_port,"Default port used for communiation between the server and the clients"],
                ["Filesystem depth", self._filesystem_depth,"The server creates a file structure, with the given amount of depth"],
                ["File ratio", self._file_ratio,"Percent of files per level"],
                ["Directory ratio", self._directory_ratio,"Percent of directories per level"],
                ["Average entity per directory", self._average_entity_per_directory,"Amount of entities per level"],
                ["Logging", self._logging,"Enable logging and creation of log files"],
                ["Allowed users", self._allowed_users,"Allowed users for parallel usage"],
                ["Extended log on disconnect", self._allowed_users,"Creates CSV,JSON files about the commands the client interaction when the client disconnects."],
         ]}


file = open("./config.json")
config = json.loads(file.read())
file.close()
configuration = Configuration(config["server_type"],config["command_port"],config["filesystem_depth"],config["file_ratio"],config["directory_ratio"],config["average_entity_per_directory"],config["logging"],config["allowed_users"],config["extended_log_on_disconnect"],config["modification_minutes_from"],config["modification_minutes_to"],config["different_structure_per_client"],config["file_byte_size_min"],config["file_byte_size_max"])