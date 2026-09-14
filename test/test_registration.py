import pytest
from models.user_dto import User
from utils.conftest import  *


class TestRegistration:

    def test_registration_positive(self, session, registration_url, random_user):
        print(random_user)
        body = {
            "username": random_user.username,
            "password": random_user.password,
        }
        headers = {
            "Content-Type": "application/json",
        }
        response = session.post(registration_url, json=body, headers=headers)
        assert response.status_code == 200
        assert "token" in response.json().keys()

    def test_registration_negative_duplicate_user(self, session, registration_url, random_user):
        body = {
            "username": random_user.username,
            "password": random_user.password,
        }
        headers = {
            "Content-Type": "application/json",
        }
        session.post(registration_url, json=body, headers=headers)
        response = session.post(registration_url, json=body, headers=headers)
        print(response.json())
        assert response.status_code in [400, 409]
        assert "User already exists" in response.json().values()

    def test_email_and_password_positive(self, session, registration_url):
        body = {
            "username": "fort@my.au",
            "password": "Regeno@13",
        }
        headers = {
            "Content-Type": "application/json",
        }
        response = session.post(registration_url, json=body, headers=headers)
        print(response.json())
        assert response.status_code == 200