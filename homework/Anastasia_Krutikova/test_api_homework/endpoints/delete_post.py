import requests
import allure

from test_api_homework.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('Delete a post')
    def delete_a_post(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        # print(f'{object_id}')
        return self.response
