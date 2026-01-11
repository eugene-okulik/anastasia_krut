import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint

class UpdatePost(Endpoint):

    @allure.step('Get a post')
    def make_changes_in_post(self,body,object_id):
        self.response = requests.put(f'{self.url}/{object_id}', json=body)
        return self.response
