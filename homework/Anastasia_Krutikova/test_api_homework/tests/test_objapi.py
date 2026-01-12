import pytest


TEST_DATA = [
    {
        "name": 'Anastasia',
        "data": {
            "city": 'St.Petersburg',
            "zip": '18934524'
        }
    },

    {
        "name": 'Julia',
        "data": {
            "city": 'Moscow',
            "zip": '4456346'
        }
    }
]

TEST_DATA_UPDATE = [
    {
        "name": 'Anastasia',
        "data": {"city": 'St.Petersburg UPD', "zip": '18934524'}
    }
]

TEST_PATCH_DATA = [
    {
        "data": {
            "city": "St.Petersburg PATCHED",
        }
    }
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_status_code_is_200()


def test_get_object(get_object_endpoint, object_id):
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_200()


def test_update_object(update_object_endpoint, object_id):
    update_body = TEST_DATA_UPDATE[0]

    update_object_endpoint.update_object_by_id(update_body, object_id)
    update_object_endpoint.check_status_code_is_200()


def test_patch_object(patch_object_endpoint, object_id):
    patch_body = TEST_PATCH_DATA[0]

    patch_object_endpoint.patch_object_by_id(patch_body, object_id)
    patch_object_endpoint.check_status_code_is_200()


def test_delete_object(delete_object_endpoint, create_object_for_delete):
    delete_object_endpoint.delete_object_by_id(create_object_for_delete)
    delete_object_endpoint.check_status_code_is_200()
