import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint

class GetPost(Endpoint):

    @allure.step('Get a post')
    def get_post_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        #print(f'{object_id}')
        return self.response
