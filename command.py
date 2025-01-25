import re
from responses import RESPONSES
class Command:

    def __init__(self,_command:bytes):
        self._plain_command = _command.decode('utf-8')
        _command_temporary = re.split('\s+', self._plain_command)
        self._command = _command_temporary[0]
        self._parameters = list()
        if len(_command_temporary) > 1:
            self._parameters = _command_temporary[0::]
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
        command_response = RESPONSES[self._command]
        if "default" not in command_response:
            return []
        current_response = command_response["default"]
        return_data = []
        for i in range(len(current_response)):
            one_response = current_response[i]
            for p in _parameters.keys():
                one_response["content"] = one_response["content"].replace("_"+p.upper()+"_",str(_parameters[p]))
            pass
            return_data.append(one_response)
        print("return_data")
        print(return_data)
        return return_data