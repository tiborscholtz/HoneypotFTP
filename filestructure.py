from math import ceil, floor
import random
import string
from constants import DIRECTORIES
from constants import FILE_TYPES
from entityFile import EntityFile
from entityFolder import EntityFolder
from datetime import datetime, timedelta
from configuration import configuration


class FileStructure:
    def __init__(self,_filesystem_depth,_file_ratio,_directory_ratio,_average_entity_per_directory):
        self._current_datetime = datetime.now()
        self._structure = list()
        self._filesystem_depth = _filesystem_depth
        self._file_ratio = _file_ratio
        self._directory_ratio = _directory_ratio
        self._average_entity_per_directory = _average_entity_per_directory
        self._letters = string.ascii_uppercase + string.digits
        self._structure = self.generate_directory_structure(self._filesystem_depth,[],"root")
        pass
        
    def generate_directory_structure(self,_remaining_depth,_directory,parent_dir_name):
        if _remaining_depth == 0:
            return []
        directory_per_level = ceil((self._average_entity_per_directory / 100) * (self._directory_ratio * 100))
        file_per_level = ceil((self._average_entity_per_directory / 100) * (self._file_ratio * 100))
        for d in range(directory_per_level):
            d = self.get_random_past_date()
            data = self.generate_data_based_on_parent_dir(parent_dir_name)
            directory = EntityFolder(True,True,True,True,False,True,True,False,True,"1",self.get_data_owner(),self.get_data_owner(),4096,d,data["name"])
            directory._entries = self.generate_directory_structure(_remaining_depth-1,directory._entries,data["name"])
            _directory.append(directory)
            pass
        for f in range(file_per_level):
            d = self.get_random_past_date()
            data = self.generate_data_based_on_parent_dir(parent_dir_name)
            file = EntityFile(True,True,True,True,False,True,True,False,True,"1",self.get_data_owner(),self.get_data_owner(),self.get_random_size(),d,data["name"],data["extension"])
            _directory.append(file)
            pass
        return _directory

    def generate_data_based_on_parent_dir(self,_sent_parent_dir) -> dict:
        data = {"name":self.generate_name(),"extension":"txt"}
        if _sent_parent_dir not in DIRECTORIES:
            return data
        data["extension"] = random.choice(DIRECTORIES[_sent_parent_dir]["files"])
        if data["extension"] not in FILE_TYPES:
            return data
        data["name"] = random.choice(FILE_TYPES[data["extension"]])
        return data
    def generate_name(self,length = 10):
        random_name = ""
        for i in range(length):
            random_name += random.choice(self._letters)
        return random_name
    
    def get_data_owner(self):
        return "www-data"
    
    def get_random_past_date(self):
        return (self._current_datetime.today() - timedelta(minutes=random.randint(configuration.get_modification_minutes_from(),configuration.get_modification_minutes_to()))).strftime("%b %d %H:%M")

    def get_random_size(self):
        return random.randint(configuration.get_file_byte_size_min(),configuration.get_file_byte_size_max())

    def get_output(self,_elements = None,padding = 0):
        repeat_string = "\t" * padding
        padding = padding + 1
        _elements = self._structure if _elements is None else _elements
        for i in range(len(_elements)):
            if _elements[i].is_directory():
                self.get_output(_elements[i]._entries,padding)
