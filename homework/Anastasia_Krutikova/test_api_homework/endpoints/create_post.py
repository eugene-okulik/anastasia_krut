import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint

class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self,body):
        self.response = requests.post(self.url,json=body)
        return self.response
