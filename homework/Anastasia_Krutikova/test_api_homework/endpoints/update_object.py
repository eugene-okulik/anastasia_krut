import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update object')
    def update_object_by_id(self, body, object_id):
        self.response = requests.put(f'{self.url}/{object_id}', json=body)
        return self.response
