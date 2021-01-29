from .naiive_post_manager import NaiivePostManager
from .sql_post_manager import SQLPostManager
from .unknown_post_manager import UnknownPostManager


class PostFactory:
    def __init__(self):
        self.type = "NAIIVE"

    def set_type(self, new_type):
        self.type = new_type
        return self

    def new(self):
        if self.type == "NAIIVE":
            return NaiivePostManager()
        elif self.type == "SQL":
            return SQLPostManager()
        else:
            return UnknownPostManager()
