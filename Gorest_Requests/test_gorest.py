
from datetime import datetime
import requests
import yaml

now = datetime.now()
random_text = now.strftime("%H%M%S")

name = "name" + random_text,
email = "www." + random_text + "name@emale.com",
gender = "male",
status = "active"

class Test(object):
    format = "json"
    url = "https://gorest.co.in/public/v2/users/"

    def setup_method(self):
        key_file = open("key.yaml", "r")
        setting = yaml.safe_load(key_file)
        self.access_token = setting["key"]

    def test_requests(self):

        # Get users list, status code is 200
        params = {"format": format, "access-token": self.access_token}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

        # Get users list, status code is 404
        params = {"format": format, "access-token": self.access_token, "accept": "application/json"}
        response = requests.patch(self.url, params=params)
        assert response.status_code == 404

        # Create a user, status code is 201
        data = {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status
        }
        params = {"format": self.format, "access-token": self.access_token}
        response = requests.post(self.url, params=params, data=data)
        assert response.status_code == 201
        r = response.json()
        user_id = (r["id"])

        # Get a user, status code is 200
        params = {"format": self.format, "access-token": self.access_token, "name": name}
        response = requests.get(self.url, params=params)
        assert response.status_code == 200

        # Try to get a user, status code is 400
        headers = {"Host": ""}
        params = {"format": self.format, "access-token": self.access_token, "name": name}
        response = requests.get(self.url, params=params, headers=headers)
        assert response.status_code == 400

        # Try to create an existing user, status code is 422
        params = {"format":self.format,"access-token":self.access_token,}
        response = requests.post(self.url, params=params, data=data)
        assert response.status_code == 422

        # Try to create a user with wrong token, status code is 401
        params = {"format":self.format,"access-token":"safa",}
        response = requests.post(self.url, params=params, data=data)
        assert response.status_code == 401

    # Delete a user, status code is 204
        params = {"format":self.format,"access-token":self.access_token}
        response = requests.delete(self.url + str(user_id), params=params)
        assert response.status_code == 204
