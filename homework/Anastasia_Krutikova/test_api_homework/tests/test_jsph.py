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
def test_post_object(create_post_endpoint, data, delete_a_post):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_status_code_is_200()

    object_id = create_post_endpoint.get_object_id()
    delete_a_post.delete_a_post(object_id)


def test_get_a_post(get_post_endpoint, create_post_endpoint, delete_a_post):
    create_body = TEST_DATA[0]
    create_post_endpoint.create_new_post(create_body)
    object_id = create_post_endpoint.get_object_id()
    get_post_endpoint.get_post_by_id(object_id)
    get_post_endpoint.check_status_code_is_200()

    delete_a_post.delete_a_post(object_id)


def test_put_object(update_post_endpoint, create_post_endpoint, delete_a_post):
    create_body = TEST_DATA[0]
    create_post_endpoint.create_new_post(create_body)
    object_id = create_post_endpoint.get_object_id()

    update_body = TEST_DATA_UPDATE[0]
    update_post_endpoint.make_changes_in_post(update_body, object_id)
    update_post_endpoint.check_status_code_is_200()

    delete_a_post.delete_a_post(object_id)


def test_patch_object(patch_post_endpoint, create_post_endpoint, delete_a_post):
    create_body = TEST_DATA[0]
    create_post_endpoint.create_new_post(create_body)
    object_id = create_post_endpoint.get_object_id()

    patch_body = TEST_PATCH_DATA[0]
    patch_post_endpoint.patch_post(patch_body, object_id)
    patch_post_endpoint.check_status_code_is_200()

    delete_a_post.delete_a_post(object_id)


def test_delete_data(create_post_endpoint, delete_a_post):
    create_body = TEST_DATA[0]
    create_post_endpoint.create_new_post(create_body)
    object_id = create_post_endpoint.get_object_id()

    delete_a_post.delete_a_post(object_id)
    delete_a_post.check_status_code_is_200()
