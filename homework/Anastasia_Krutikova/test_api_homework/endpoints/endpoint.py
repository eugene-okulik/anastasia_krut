import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None

    @allure.step('Check status code is correct')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Get object_id')
    def get_object_id(self):
        object_id = self.response.json()['id']
        return object_id

    @allure.step('Check object_id_is_correct')
    def check_object_id_is_correct(self, object_id):
        assert self.response.json()['id'] == object_id
