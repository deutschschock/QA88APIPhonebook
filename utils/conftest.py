import pytest
import requests
import time
import random
from utils.config import *
from faker import Faker

from models.user_dto import User

fake = Faker()

@pytest.fixture(scope="session")
def registration_url():
    return BASE_URL + API_VERSION + REGISTRATION_URL
@pytest.fixture(scope="session")
def login_url():
    return BASE_URL + API_VERSION + LOGIN_URL
@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    yield s  #передать данные в тест
    s.close()

@pytest.fixture(scope="function")
def random_user():
    username = f"qa_{int(time.time())}_{fake.email()}"
    password = fake.password(length=random.randrange(8, 15),
                             special_chars=False,
                             digits = True,
                             upper_case = True,
                             lower_case=True
                             )+'$'
    yield User(username=username, password=password)
