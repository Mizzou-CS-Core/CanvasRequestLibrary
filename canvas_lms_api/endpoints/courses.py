from canvas_lms_api.models.course import Course
from typing import Optional
class CourseService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    def get_course(self, course_id: int, return_json: bool = False, includes: Optional[list[str]] = None,):
        q = ""
        if includes:
            q = "?" + "&".join(f"include={i}" for i in includes)
        endpoint: str = f"courses/{course_id}{q}"
        json = self._api_client.request("GET", endpoint)
        if return_json:
            return json
        return Course.from_json(json)
    def get_people_from_course(self, course_id: int, return_json: bool = False, per_page: int=100)
        options = f"per_page={per_page}"
        endpoint: str = f"courses/{course_id}/search_users?{options}"
        json = self._api_client.request("GET", endpoint)
        if return_json:
            return json
        return Person.parse_people_from_json(json)