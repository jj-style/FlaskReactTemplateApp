from abc import ABC, abstractmethod


class PostManager(ABC):
    """Defines useful methods for acting on posts from the post resource"""

    @abstractmethod
    def list_posts(self):
        """Returns list of posts"""
        pass

    @abstractmethod
    def get_post_by_id(self, id):
        """Returns a single post given by it's id"""
        pass

    @abstractmethod
    def create_post(self, req):
        """Creates a new post"""
        pass

    @abstractmethod
    def get_post_by_slug(self, slug: str):
        """Returns a post by it's slug"""
        pass
