from locust import task, HttpUser
import random


class TestObjects(HttpUser):

    object_id = None

    @task(5)
    def get_all_objects(self):
        self.client.get('/object')

    @task(5)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice([12673, 12674, 12675, 12676])}')

    @task(10)
    def create_object(self):

        data = {
            "name": f"Test_{random.randint(100, 999)}",
            "data": {
                "city": random.choice(['St.Petersburg', 'Moscow']),
                "zip": f"{random.randint(10000, 99999)}"
            }
        }
        response = self.client.post('/object', json=data)
        self.object_id = response.json().get('id')

    @task(2)
    def put_object(self):

        if self.object_id:
            data = {
                "name": f"Test_{random.randint(100, 999)}",
                "data": {
                    "city": 'St.Petersburg UPD',
                    "zip": f"UPDATE_{random.randint(10000, 99999)}"
                }
            }
            self.client.put(f'/object/{self.object_id}', json=data)

    @task(2)
    def patch_object(self):

        if self.object_id:
            data = {
                "data": {
                    "zip": f"PATCHED_{random.randint(10000, 99999)}"
                }
            }
            self.client.patch(f'/object/{self.object_id}', json=data)

    @task(2)
    def delete_object(self):

        if self.object_id:
            self.client.delete(f'/object/{self.object_id}')
            self.object_id = None
