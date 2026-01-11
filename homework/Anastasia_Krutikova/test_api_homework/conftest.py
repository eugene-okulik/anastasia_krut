import pytest

from .endpoints.create_post import CreatePost
from .endpoints.update_post import UpdatePost
from .endpoints.get_post import GetPost
from .endpoints.delete_post import DeletePost
from .endpoints.patch_post import PatchPost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()

@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()

@pytest.fixture()
def get_post_endpoint():
    return GetPost()

@pytest.fixture()
def delete_a_post():
    return DeletePost()
