import re
class Command:

    def __init__(self,_command):
        self._plain_command = _command
        _command_temporary = re.split('\s+', _command)
        self._command = _command_temporary[0]
        self._parameters = list()
        if len(_command_temporary) > 1:
            self._parameters = _command_temporary[0::]
        pass

    def is_command(self,_command_to_compare):
        return _command_to_compare == self._command
    
    def get_parameter_at_index(self,_index):
        return self._parameters[_index]
    
    def has_parameter_at_index(self,_index):
        return self._parameters[_index] is not None
    
    def has_parameters(self):
        return len(self._parameters) > 0