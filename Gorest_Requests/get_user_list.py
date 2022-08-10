
import requests
import pytest
import yaml

class Test(object):
    format = "json"
    url = "https://gorest.co.in/public/v2/users"

    def setup_method(self):
        key_file = open("key.yaml", "r")
        setting = yaml.safe_load(key_file)
        self.access_token = setting["key"]

    def test_get_users(self):
        params = {"format": format, "access-token": self.access_token}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

    @pytest.mark.parametrize("user_id",[3425])
    def test_get_a_user(self, user_id):
        params = {"format":self.format,"access-token":self.access_token,"id":user_id}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200
