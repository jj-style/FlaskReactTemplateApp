import pytest

from .post_factory import PostFactory
from .post_manager import PostManager


@pytest.fixture(scope="module")
def naiive_post_manager() -> PostManager:
    f = (PostFactory()).set_type("NAIIVE")
    return f.new()


def test_list_no_posts_happy(naiive_post_manager: PostManager):
    res = naiive_post_manager.list_posts()
    assert type(res) == list
    assert len(res) == 0


def test_get_post_by_id_404(naiive_post_manager: PostManager):
    res = naiive_post_manager.get_post_by_id("randomid_that_doesnt_exist")
    assert 404 in res


def test_create_post(naiive_post_manager: PostManager):
    res = naiive_post_manager.create_post({"title": "my post", "body": "body of post"})
    assert 201 in res


def test_get_by_id(naiive_post_manager: PostManager):
    res = naiive_post_manager.get_post_by_id(0)
    assert type(res) == dict
    assert res.get("title") == "my post"
    assert res.get("body") == "body of post"


def test_get_by_slug(naiive_post_manager: PostManager):
    res = naiive_post_manager.get_post_by_slug("my-post")
    assert type(res) == dict
    assert res.get("title") == "my post"
    assert res.get("body") == "body of post"
