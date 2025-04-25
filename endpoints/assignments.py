from  CanvasRequestLibrary.models.assignment import Assignment

class AssignmentService:
    def __init__(self, api_client) -> None:
        self._api_client = api_client
    
    def get_assignments_from_course(self, course_id: int, per_page: int = 10, return_json: bool = False):
        options = f"per_page={per_page}"
        endpoint: str = f"courses/{str(course_id)}/assignments?{options}"
        json = self._api_client.request("GET", endpoint)
        if (return_json):
            return json
        return Assignment.parse_json_into_assignments(assignment_json=json)
    
