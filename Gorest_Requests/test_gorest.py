from datetime import datetime
from API.api_methods import Methods


class Tests(Methods):
    now = datetime.now()
    random_text = now.strftime("%H%M%S")
    name = "name" + random_text,
    email = "www." + random_text + "name@email.com",
    gender = "male",
    status = "active"
    format = "json"

    def test_requests(self):
        # Get list users, status code is 200
        params = {"format": self.format, "access-token": self.access_token}
        assert Methods.get(self, params).status_code == 200

        # Create user, status code is 201
        data = {
            "name": self.name,
            "email": self.email,
            "gender": self.gender,
            "status": self.status}
        response = Methods.post(self, params, data)
        assert response.status_code == 201
        r = response.json()
        user_id = (r["id"])

        # Get user, status code is 200
        params = {"format": self.format, "access-token": self.access_token, "name": self.name}
        assert Methods.get(self, params).status_code == 200

        # Update user with put request, status code is 200
        data = {"gender": "female"}
        assert Methods.put(self, params, data, user_id).status_code == 200

        # Update user with patch request, status code is 200
        data = {"gender": "male"}
        assert Methods.patch(self, params, data, user_id).status_code == 200

        # Try to get a user, status code is 400
        headers = {"Host": ""}
        params = {"format": self.format, "access-token": self.access_token}
        assert Methods.get_with_headers(self, params, headers).status_code == 400

        # Try to create an existing user, status code is 422
        assert Methods.post(self, params, data).status_code == 422

        # Try to create a user with wrong token, status code is 401
        params = {"format": self.format, "access-token": "safa"}
        assert Methods.post(self, params, data).status_code == 401

        # Delete user, status code is 204
        params = {"format": self.format, "access-token": self.access_token}
        assert Methods.delete(self, params, user_id).status_code == 204

        # Get deleted user, status code is 404
        params = {"format": self.format, "access-token": self.access_token}
        assert Methods.get_with_id(self, params, user_id).status_code == 404
