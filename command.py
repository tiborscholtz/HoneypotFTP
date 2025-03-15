import re
from responses import RESPONSES
import copy
class Command:

    def __init__(self,_command:bytes):
        self._plain_command = _command.decode('utf-8').strip()
        _command_temporary = re.split('\s+', self._plain_command)
        self._command = _command_temporary[0]
        self._parameters = list()
        if len(_command_temporary) > 1:
            self._parameters = _command_temporary[1::]
        pass

    def is_command(self,_command_to_compare) -> bool:
        return _command_to_compare == self._command
    
    def get_parameter_at_index(self,_index) -> any:
        return self._parameters[_index]
    
    def has_parameter_at_index(self,_index) -> bool:
        return self._parameters[_index] is not None
    
    def has_parameters(self) -> bool:
        return len(self._parameters) > 0
    
    def get_parameters_length(self) -> int:
        return len(self._parameters)

    def get_response(self,_parameters) -> list:
        if self._command not in RESPONSES:
            return []
        command_response = copy.deepcopy(RESPONSES[self._command])
        if "default" not in command_response:
            return []
        current_response = copy.deepcopy(command_response["default"])
        return_data = []
        for i in range(len(current_response)):
            one_response = copy.deepcopy(current_response[i])
            handled = False
            for key, value in _parameters.items():
                if handled == True:
                    continue
                if "_"+key.upper()+"_" == one_response["content"]:
                    one_response["content"] = value
                    handled = True
                    continue
                if isinstance(value,(str)) == False:
                    value = str(_parameters[key])
                one_response["content"] = one_response["content"].replace("_"+key.upper()+"_",value)
            pass
            return_data.append(one_response)
        return return_data