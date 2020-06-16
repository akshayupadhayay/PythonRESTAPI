import requests
import json
import jsonpath
from test_config import URL
import datetime


def test_UpdateUser():

    # Read Input from Json file
    file = open('../../../data/putData.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make PUT request with Json Input Body
    response = requests.put(URL.PUT_URL, request_json)
    # Validating response code
    assert response.status_code == 200
    # Parse response Content
    response_json: object = json.loads(response.text)
    print(response_json)
    # Fetch a Json key
    new_name = jsonpath.jsonpath(response_json, 'name')
    assert new_name[0] == "morpheus new update"
