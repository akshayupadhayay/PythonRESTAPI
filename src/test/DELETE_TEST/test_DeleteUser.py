import requests
from test_config import URL


def test_DeleteUser():

    response = requests.delete(URL.DELETE_URL)
    # Fetch response code
    print(response.status_code)
    assert response.status_code == 204
