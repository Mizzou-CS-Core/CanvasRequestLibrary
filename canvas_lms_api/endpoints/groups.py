from CanvasRequestLibrary.models.group import Group
from CanvasRequestLibrary.models.person import Person
class GroupService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    def get_groups_from_course(self, course_id: int, return_json: bool = False):
        endpoint: str = f"courses/{str(course_id)}/groups"
        json = self._api_client.request("GET", endpoint)
        if return_json:
            return json
        return Group.parse_groups_from_json(json)
    def get_people_from_group(self, group_id: int, per_page: int = 50, return_json: bool = False):
        options = f"per_page={per_page}"
        endpoint: str = f"groups/{group_id}/users?{options}"
        json = self._api_client.request("GET", endpoint)
        if return_json:
            return json
        return Person.parse_people_from_json(people_json=json)