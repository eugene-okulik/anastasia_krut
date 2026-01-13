import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Patch an object')
    def patch_object_by_id(self, body, object_id):
        self.response = requests.patch(f'{self.url}/{object_id}', json=body)
        return self.response
