from .post_manager import PostManager
from flask import url_for
from app.data import post_response, posts_response, new_post_request


class NaiivePostManager(PostManager):
    def __init__(self):
        self.posts = [{"id": 1, "title": "post title", "body": "body of post"}]

    def list_posts(self):
        posts = [{**p, **{"uri": url_for("post_ep", id=p["id"])}} for p in self.posts]
        return posts_response.dump(posts)

    def get_post_by_id(self, id):
        p = next((p for p in self.posts if p["id"] == id), None)
        if not p:
            return "Not Found", 404
        else:
            p = {**p, **{"uri": url_for("post_ep", id=p["id"])}}
            return post_response.dump(p)

    def create_post(self, req):
        post = self.new_post_request.load(req)
        ids = [p.id for p in self.posts]
        self.posts.append({**post, **{"id": max(ids) + 1}})

    def get_post_by_slug(self, slug: str):
        p = next((p for p in self.posts if p.get("slug", "") == slug), None)
        if not p:
            return "Not Found", 404
        else:
            p = {**p, **{"uri": url_for("post_ep", id=p["id"])}}
            return post_response.dump(p)
