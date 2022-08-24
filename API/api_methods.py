import requests
import yaml


class Methods:
    url = "https://gorest.co.in/public/v2/users/"

    def setup_method(self):
        key_file = open("key.yaml", "r")
        setting = yaml.safe_load(key_file)
        self.access_token = setting["key"]

    def get(self, params):
        response = requests.get(self.url, params=params)
        return response

    def get_with_id(self, params, user_id):
        response = requests.get(self.url + str(user_id), params=params)
        return response

    def get_with_headers(self, params, headers):
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def post(self, params, data):
        response = requests.post(self.url, params=params, data=data)
        return response

    def put(self, params, data, user_id):
        response = requests.put(self.url + str(user_id), params=params, data=data)
        return response

    def patch(self, params, data, user_id):
        response = requests.patch(self.url + str(user_id), params=params, data=data)
        return response

    def delete(self, params, user_id):
        response = requests.delete(self.url + str(user_id), params=params)
        return response
