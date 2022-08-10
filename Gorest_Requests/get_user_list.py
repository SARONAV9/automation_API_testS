
import requests
import yaml

class Test(object):
    format = "json"
    test_url = "https://gorest.co.in/public/v2/users"

    def setup_method(self):
        key_file = open("key.yaml", "r")
        setting = yaml.safe_load(key_file)
        self.access_token = setting["key"]

    def test_get_users(self):
        params = {"format": format, "access-token": self.access_token}
        response = requests.get(self.test_url, params=params)
        assert response.status_code == 200
