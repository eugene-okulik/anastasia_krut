import pytest

from .endpoints.create_object import CreateObject
from .endpoints.update_object import UpdateObject
from .endpoints.get_object import GetObject
from .endpoints.delete_object import DeleteObject
from .endpoints.patch_object import PatchObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_object_for_delete(create_object_endpoint):

    body = {
        "name": "Test Object",
        "data": {
            "city": "Test City",
            "zip": "12345"
        }
    }

    response = create_object_endpoint.create_new_object(body)

    yield response.json()['id']


@pytest.fixture()
def object_id(create_object_endpoint, delete_object_endpoint):

    body = {
        "name": "Test Object",
        "data": {
            "city": "Test City",
            "zip": "12345"
        }
    }
    create_object_endpoint.create_new_object(body)

    object_id = create_object_endpoint.get_object_id()

    yield object_id

    delete_object_endpoint.delete_object_by_id(object_id)
