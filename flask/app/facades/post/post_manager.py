from abc import ABC, abstractmethod


class PostManager(ABC):
    @abstractmethod
    def list_posts(self):
        pass

    @abstractmethod
    def get_post_by_id(self):
        pass

    @abstractmethod
    def create_post(self, req):
        pass

    @abstractmethod
    def get_post_by_slug(self, slug):
        pass
