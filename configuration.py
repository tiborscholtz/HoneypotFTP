class Configuration:
    def __init__(self,_type, _data_port,_command_port,_filesystem_depth,_file_ratio,_directory_ratio,_average_entity_per_directory,_logging,_allowed_users):
        self._type = _type
        self._data_port = _data_port
        self._command_port = _command_port
        self._filesystem_depth = _filesystem_depth
        self._file_ratio = _file_ratio
        self._directory_ratio = _directory_ratio
        self._average_entity_per_directory = _average_entity_per_directory
        self._logging = _logging
        self._allowed_users = _allowed_users
        pass
    
    def get_type(self):
        return self._type

    def get_data_port(self):
        return self._data_port
    
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
    
    def get_object_format(self):
        return {
            "headers": ["Property", "Value","Description"],
            "data": [
                ["Type",self._type,"HoneyFTP can emulate several FTP server's response palette."],
                ["Data port",self._data_port,"TODO"],
                ["Command port", self._command_port,"Default port used for communiation between the server and the clients"],
                ["Filesystem depth", self._filesystem_depth,"The server creates a file structure, with the given amount of depth"],
                ["File ratio", self._file_ratio,"Percent of files per level"],
                ["Directory ratio", self._directory_ratio,"Percent of directories per level"],
                ["Average entity per directory", self._average_entity_per_directory,"Amount of entities per level"],
                ["Logging", self._logging,"Enable logging and creation of log files"],
                ["Allowed users", self._allowed_users,"Allowed users for parallel usage"],
         ]}
