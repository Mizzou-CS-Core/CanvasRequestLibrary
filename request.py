
import requests

CANVAS_BASE_URL = "https://umsystem.instructure.com/api/"

def canvas_api_call(endpoint: str, token: str, headers=None):
    auth_header: dict[str, str] = {'Authorization': 'Bearer ' + token}
    qualified_url: str = CANVAS_BASE_URL + endpoint
    if headers is None:
        response = requests.get(url=qualified_url, headers=auth_header)
    else:
        response = requests.get(url=qualified_url, headers=headers + auth_header)
    response.raise_for_status() 
    return None