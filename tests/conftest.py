import pytest
import requests
from handle import Handle
from urls import Urls
from generator import register_new_courier


@pytest.fixture
def courier_data():
    data = register_new_courier()
    yield data
    # Удаление курьера после теста
    login_response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json={
        "login": data["login"],
        "password": data["password"]
    })
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        requests.delete(f'{Urls.URL}{Handle.CREATE_COURIER}/{courier_id}')
