from .post_manager import PostManager
from .naiive_post_manager import NaiivePostManager
from .sql_post_manager import SQLPostManager
from .unknown_post_manager import UnknownPostManager


class PostFactory:
    """Builds an implementation of a PostManager based on it's type

    Attributes:
        type (str) : The maximum speed that such a bird can attain.
    """

    def __init__(self):
        self.type: str = "NAIIVE"

    def set_type(self, new_type: str):
        self.type = new_type
        return self

    def new(self) -> PostManager:
        if self.type == "NAIIVE":
            return NaiivePostManager()
        elif self.type == "SQL":
            return SQLPostManager()
        else:
            return UnknownPostManager()
