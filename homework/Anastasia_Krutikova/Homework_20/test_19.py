import requests
import pytest


@pytest.fixture()
def new_post_object():
    body = {
        "name": "Anastasia",
        "data": {
            "city": "St.Petersburg",
            "zip": 18934524
        }
    }

    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    post_id =  response.json()['id']

    yield post_id

    print('deleting the post')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture(scope='session', autouse=True)
def start_complete():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_after():
    print("Before test")
    yield
    print("After test")


def test_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def test_one_object(new_post_object):
    object_id = new_post_object
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.json()['id'] == object_id, 'Object id is incorrect'


@pytest.mark.parametrize('name,city,zip_code', [
    ("Anastasia", "St.Petersburg", 18934524),
    ("Julia", "Moscow", 3345622),
    ("Maria", "Sochi", 345567)
])

def test_post_object(name, city, zip_code):
    body = {
        "name": name,
        "data": {
            "city": city,
            "zip": zip_code
        }
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, 'Status code is incorrect'

    object_id = response.json()['id']
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def test_put_object(new_post_object):
    object_id = new_post_object
    body = {
        "name": "Anastasia",
        "data": {
            "city": "St.Petersburg UPD",
            "zip": 18934524
        }
    }

    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['city'] == 'St.Petersburg UPD'


@pytest.mark.medium
def test_patch_object(new_post_object):
    object_id = new_post_object
    body = {
        "name": "Anastasia_upd",
    }

    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Anastasia_upd', 'Name is incorrect'


@pytest.mark.critical
def test_delete_object(new_post_object):
    object_id = new_post_object
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
