from .post_manager import PostManager
from app.data import post_response, posts_response, new_post_request


class NaiivePostManager(PostManager):
    def __init__(self):
        self.posts = []

    def list_posts(self):
        return posts_response.dump(self.posts)

    def get_post_by_id(self, id):
        p = next((p for p in self.posts if p["id"] == id), None)
        if not p:
            return "Not Found", 404
        else:
            return post_response.dump(p)

    def create_post(self, req):
        post = new_post_request.load(req)
        ids = [p.id for p in self.posts]
        if len(ids) == 0:
            ids = [-1]
        new_post = {
            **post,
            **{"id": max(ids) + 1, "slug": post["title"].replace(" ", "-").lower()},
        }
        self.posts.append(new_post)
        return new_post, 201

    def get_post_by_slug(self, slug: str):
        p = next((p for p in self.posts if p.get("slug", "") == slug), None)
        if not p:
            return "Not Found", 404
        else:
            return post_response.dump(p)
