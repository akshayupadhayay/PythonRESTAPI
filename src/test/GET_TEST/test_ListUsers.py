from typing import List, Any, Union

import requests
import json
import jsonpath
from requests.models import Response
from test_config import URL


def test_ListUsers_PageCountCheck():

    # GET Response Code
    list_response: Response = requests.get(URL.GET_URL)
    # GET Response Content
    list_response_body: bytes = list_response.content
    # GET Response Header
    list_response_header = list_response.headers
    # Parse response to Json format
    json_response: object = json.loads(list_response.text)  # OR json.loads(list_response_body)
    # Fetch value using JsonPath
    total_pages: Union[List[Any], bool] = jsonpath.jsonpath(json_response, 'total_pages')
    assert total_pages[0] == 2


def test_ListUsers_NameCheck():

    # Get Json response
    list_response: Response = requests.get(URL.GET_URL)
    # print(json.dumps(list_response.json(), indent=3))
    resp = list_response.json()
    last_names = [d['last_name'] for d in resp["data"]]
    assert last_names[0] == "Lawson"

