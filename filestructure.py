from math import ceil, floor
import random
import string
from constants import DIRECTORIES
from constants import FILE_TYPES
from entityFile import EntityFile
from entityFolder import EntityFolder


class FileStructure:
    def __init__(self,_filesystem_depth,_file_ratio,_directory_ratio,_average_entity_per_directory):
        self._structure = list()
        self._filesystem_depth = _filesystem_depth
        self._file_ratio = _file_ratio
        self._directory_ratio = _directory_ratio
        self._average_entity_per_directory = _average_entity_per_directory
        self._letters = string.ascii_uppercase + string.digits
        pass
        
    def generate_directory_structure(self):
        directory_per_level = ceil((self._average_entity_per_directory / 100) * (self._directory_ratio * 100))
        file_per_level = ceil((self._average_entity_per_directory / 100) * (self._file_ratio * 100))
        for d in range(directory_per_level):
            directory = EntityFolder(True,True,True,True,False,True,True,False,True,"10","www-data","www-data","4096","Jan 20 18:59","test")
            self._structure.append(directory)
            pass
        for f in range(file_per_level):
            file = EntityFile(True,True,True,True,False,True,True,False,True,"10","www-data","www-data","1000","Jan 20 18:59","todo","txt")
            self._structure.append(file)
            pass
        for i in range(len(self._structure)):
            print(self._structure[i].get_ls_output())
        pass

    def generate_name(self,length = 10):
        random_name = ""
        for i in range(length):
            random_name += random.choice(self._letters)
        return random_name
        pass