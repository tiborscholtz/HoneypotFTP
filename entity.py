class Entity:
    def __init__(self,_owner_read,_owner_write,_owner_execute,_group_read,_group_write,_group_execute,_other_read,_other_write,_other_execute,_link_count,_owner,_group,_size,_modified_at,_name):
        self._active = True
        self._owner_read = _owner_read
        self._owner_write = _owner_write
        self._owner_execute = _owner_execute
        self._group_read = _group_read
        self._group_write = _group_write
        self._group_execute = _group_execute
        self._other_read = _other_read
        self._other_write = _other_write
        self._other_execute = _other_execute
        self._link_count = _link_count
        self._owner = _owner
        self._group = _group
        self._size = _size
        self._modified_at = _modified_at
        self._name = _name
        pass
    
    def is_active(self):
        return self._active

    def set_active(self,_value):
        self._active = _value
    
    def get_name(self):
        return self._name
    
    def get_modified_at(self):
        return self._modified_at
    
    def get_size(self):
        return self._size
    
    def get_group(self):
        return self._group
    
    def get_owner(self):
        return self._owner
    
    def get_owner_read(self):
        return self._owner_read
    
    def get_owner_write(self):
        return self._owner_write
    
    def get_owner_execute(self):
        return self._owner_execute
    
    def get_group_read(self):
        return self._group_read
    
    def get_group_write(self):
        return self._group_write
    
    def get_group_execute(self):
        return self._group_execute
    
    def get_other_read(self):
        return self._other_read
    
    def get_other_write(self):
        return self._other_write
    
    def get_other_execute(self):
        return self._other_execute
    
    def get_link_count(self):
        return self._link_count
    
    def is_name_equal(self,_sent_name):
        if hasattr(self,"_is_directory"):
            return _sent_name == self._name
        return (self._name + "." + self._extension) == _sent_name
    def is_directory(self):
        return hasattr(self,"_is_directory")
    def get_ls_simplified(self):
        return_value = ""
        return_value += self._name
        if hasattr(self,"_extension"):
            return_value += "." + self._extension
        return return_value
    def get_ls_output(self):
        return_value = ""
        if hasattr(self,"_is_directory"):
            return_value += "d"
        else:
            return_value += "-"
        return_value += "r" if self._owner_read == True else "-"
        return_value += "w" if self._owner_write == True else "-"
        return_value += "x" if self._owner_execute == True else "-"
        return_value += "r" if self._group_read == True else "-"
        return_value += "w" if self._group_write == True else "-"
        return_value += "x" if self._group_execute == True else "-"
        return_value += "r" if self._other_read == True else "-"
        return_value += "w" if self._other_write == True else "-"
        return_value += "x" if self._other_execute == True else "-"
        return_value += "\t"
        return_value += str(self._link_count)
        return_value += "\t"
        return_value += self._owner
        return_value += "\t"
        return_value += self._group
        return_value += "\t"
        return_value += str(self._size)
        return_value += "\t"
        return_value += self._modified_at
        return_value += "\t"
        return_value += self._name
        if hasattr(self,"_extension"):
            return_value += "." + self._extension
        return return_value