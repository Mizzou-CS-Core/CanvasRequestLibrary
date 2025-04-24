class GroupService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    def get_groups_from_course(self, course_id: int):
        endpoint: str = f"courses/{str(course_id)/groups}"
        return self._api_client.request("GET", endpoint)