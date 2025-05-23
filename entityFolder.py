from entity import Entity

class EntityFolder(Entity):
    def __init__(self,_owner_read,_owner_write,_owner_execute,_group_read,_group_write,_group_execute,_other_read,_other_write,_other_execute,_link_count,_owner,_group,_size,_modified_at,_name):
        self._is_directory = True
        self._entries = list()
        super().__init__(_owner_read,_owner_write,_owner_execute,_group_read,_group_write,_group_execute,_other_read,_other_write,_other_execute,_link_count,_owner,_group,_size,_modified_at,_name)