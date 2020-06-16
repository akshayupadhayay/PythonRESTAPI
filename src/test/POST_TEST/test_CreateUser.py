import requests
import json
import jsonpath
from test_config import URL
import pytest
import sys


def test_User_One():

    # Read Input from Json file
    file = open('../../../data/postData.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input Body
    response = requests.post(URL.CREATE_URL, request_json)
    print(response.headers)
    print("\n")
    # Validating response code
    assert response.status_code == 201


def test_User_Two():

    # Read Input from Json file
    file = open('../../../data/postData.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input Body
    response = requests.post(URL.CREATE_URL, request_json)
    assert response.headers.get('Connection') == "keep-alive"


