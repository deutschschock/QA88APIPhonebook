import pytest

from utils.config import  *
from utils.conftest import *

class TestLogin:

    def test_login_positive(self, session, login_url, registered_user):
        body = {
            "username": registered_user.username,
            "password": registered_user.password,
        }
        headers = {"Content-Type": "application/json"}
        response = session.post(login_url, json=body, headers=headers)
        assert response.status_code == 200
        assert "token" in response.json().keys()

    @pytest.mark.parametrize("invalid_username", [
        "",
        "PASSWORD123"
    ])
    def test_login_negative(self, session, login_url, invalid_username):
        body = {
            "username": invalid_username,
            "password": TEST_PASSWORD,
        }
        response = session.post(login_url, json=body)
        print(response.json())
        assert response.status_code in [401, 403]
        assert "Login or Password incorrect" in response.json().values()
