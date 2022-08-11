
from datetime import datetime
import requests
import pytest
import yaml

now = datetime.now()
random_text = now.strftime("%H%M%S")

name = "name" + random_text,
email = "www." + random_text + "name@emale.com",
gender = "male",
status = "active"

class Test(object):
    format = "json"
    url = "https://gorest.co.in/public/v2/users"

    def setup_method(self):
        key_file = open("key.yaml", "r")
        setting = yaml.safe_load(key_file)
        self.access_token = setting["key"]

    def test_get_users_code_200(self):
        params = {"format": format, "access-token": self.access_token}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

    @pytest.mark.parametrize("user_id",[3425])
    def test_get_a_user_code_200(self, user_id):
        params = {"format":self.format,"access-token":self.access_token,"id":user_id}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

    # Create a user, get status code 201
    def test_create_a_user(self):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data = {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status
        }
        params = {"format": self.format, "access-token": self.access_token}
        response = requests.post(self.url, params=params, data=data)
        print(response.json())
        assert response.status_code == 201
        params = {"format": self.format, "access-token": self.access_token, "name": name}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

        # Try to create an existing user, get status code 422
        params = {"format":self.format,"access-token":self.access_token,}
        response = requests.post(self.url, params=params, data=data)
        assert response.status_code == 422

        # Create a user with wrong token, get status code 401
        params = {"format":self.format,"access-token":"safa",}
        response = requests.post(self.url, params=params, data=data)
        assert response.status_code == 401