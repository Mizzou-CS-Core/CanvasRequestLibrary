

class AssignmentService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    
    def get_assignments_from_course(self, course_id: int, per_page: int = 10):
        options = f"per_page={per_page}"
        endpoint: str = f"courses/{str(course_id)}/assignments?{options}"
        return self._api_client.request("GET", endpoint)
    
