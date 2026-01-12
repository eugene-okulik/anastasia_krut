import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        #print(f'{object_id}')
        return self.response
