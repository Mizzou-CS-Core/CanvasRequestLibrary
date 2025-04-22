
import json
from requests.models import Response


from typing import Any, final
from endpoints import (
    assignments
)
import requests

@final
class CanvasClient: 
    def __init__(self, url_base: str, token: str) -> None:
        self.url_base: str = url_base
        self.token = token
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token}",
            "User-Agent": "MyLib/1.0",
            "Accept": "application/json",
        })
        self._assignments = assignments.AssignmentService(api_client=self)
    def request(self, method: str, path: str, **kwargs):
        url: str = f"{self.url_base}{path}"
        resp: Response = self._session.request(method, url, **kwargs)
        resp.raise_for_status()
        return resp.json()








