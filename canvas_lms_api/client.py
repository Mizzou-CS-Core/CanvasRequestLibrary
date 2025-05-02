import requests
from requests.models import Response

from .endpoints import (
    assignments,
    groups,
    courses
)


class CanvasClient:
    def __init__(self, url_base: str, token: str) -> None:
        self._url_base: str = url_base
        self._token = token
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token}",
            "User-Agent": "MyLib/1.0",
            "Accept": "application/json",
        })
        self.assignments = assignments.AssignmentService(api_client=self)
        self.groups = groups.GroupService(api_client=self)
        self.courses = courses.CourseService(api_client=self)

    def request(self, method: str, path: str, **kwargs):
        url: str = f"{self._url_base}{path}"
        resp: Response = self._session.request(method, url, **kwargs)
        resp.raise_for_status()
        return resp.json()
