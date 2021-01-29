from .post_manager import PostManager


class UnknownPostManager(PostManager):
    def __init__(self):
        raise NotImplementedError(f"{__class__.__name__} cannot be constructed")

    def create_post(self, req):
        raise NotADirectoryError(f"{__class__.__name__} has no create_post")

    def get_post_by_id(self, id):
        raise NotADirectoryError(f"{__class__.__name__} has no get_post_by_id")

    def get_post_by_slug(self, slug):
        raise NotADirectoryError(f"{__class__.__name__} has no get_post_by_slug")

    def list_posts(self):
        raise NotADirectoryError(f"{__class__.__name__} has no list_posts")
