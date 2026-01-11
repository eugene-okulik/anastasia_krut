import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    @allure.step('Patch a post')
    def patch_post(self, body, object_id):
        self.response = requests.patch(f'{self.url}/{object_id}', json=body)
        return self.response
