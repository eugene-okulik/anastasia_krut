import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body):
        self.response = requests.post(self.url, json=body)
        return self.response
