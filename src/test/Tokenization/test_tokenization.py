import json
import requests
from test_config import URL


def test_tokenization():
    file = open('../../../data/RegisterToken.json', 'r')
    data = file.read()
    data = json.loads(data)
    response_post = requests.post('https://reqres.in/api/register', data, verify=False)
    response_post_json = response_post.json()
    token = response_post_json['token']

    headers = {'Authorization': 'Token ' + token}
    response_get = requests.get(URL.GET_URL, headers=headers, verify=False)
    response_get_json = json.loads(response_get.text)
    print(json.dumps(response_get_json, indent=4))
