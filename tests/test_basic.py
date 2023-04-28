import requests
import json


def test_fastapi_get():
    url = 'http://127.0.0.1:8080/'
    # login the application
    data_login = {
                "username": "FastAPIuser",
        "password": "5k5QdBhy%YLFWo42zO&J"

               }

    response_request2 = requests.get(f'{url}get_message')


def test_fastapi_post():
    url = 'http://127.0.0.1:8080/'
    # login the application
    data_login = {
                "username": "FastAPIuser",
        "password": "5k5QdBhy%YLFWo42zO&J"

               }

    data_app = {

        "firstname": "David",
        "lastname": "Balagué",
        "age": 59,
        "email": "dbalague@gmail.com"
    }
    response_request2 = requests.post(f'{url}get_user_info', json=data_app)