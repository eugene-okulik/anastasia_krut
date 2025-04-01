import requests


def all_objects():

    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


def one_object():

    object_id = new_post_object()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.json()['id'] == object_id, 'Object id is incorrect'


def post_object():

    body = {
        "name": "Anastasia",
        "data": {
        "city": "St.Petersburg",
        "zip": 18934524
        }
    }

    response = requests.post('http://167.172.172.115:52353/object', json=body)
    assert response.status_code == 200, 'Status code is incorrect'


def new_post_object():

    body = {
        "name": "Anastasia",
        "data": {
        "city": "St.Petersburg",
        "zip": 18934524
        }
    }

    response = requests.post('http://167.172.172.115:52353/object', json=body)
    return response.json()['id']


def clear(object_id):

    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def put_object():
    object_id = new_post_object()
    body = {
        "name": "Anastasia",
        "data": {
        "city": "St.Petersburg UPD",
        "zip": 18934524
        }
    }

    response = requests.put(f'http://167.172.172.115:52353/object/{object_id}', json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['city'] == 'St.Petersburg UPD'

    clear(object_id)


def patch_object():
    object_id = new_post_object()

    body = {
        "name": "Anastasia_upd",
        }

    response = requests.patch(f'http://167.172.172.115:52353/object/{object_id}', json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Anastasia_upd', 'Name is incorrect'
    clear(object_id)


def delete_object():
    object_id = new_post_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'

# all_objects()
# one_object()
# post_object()
# put_object()
# patch_object()
# delete_object()

