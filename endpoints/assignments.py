

class AssignmentService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    
    def get_assignments_from_course(self, course_id: int):
        endpoint: str = self._api_client.url_base + f"/courses/{str(course_id)}/assignments"
        return self._api_client.request("GET", endpoint)
    
