from typing import Optional

class Submission:
    def __init__(self, assignment_id: int, attempt: int, body: str, grade: str, 
                 grade_matches_current_submission: bool, html_url: str, preview_url: str, 
                 score: float, submission_type: str, submitted_at: str, user_id: int, 
                 grader_id: int, graded_at: str, late: bool, assignment_visible: bool, 
                 excused: bool, missing: bool, late_policy_status: str, points_deducted: float, 
                 seconds_late: int, workflow_state: str, extra_attempts: int, anonymous_id: str, 
                 posted_at: Optional[str], read_status: str, redo_request: bool, 
                 assignment: Optional[dict] = None, course: Optional[dict] = None, 
                 submission_comments: Optional[list] = None, url: Optional[str] = None, 
                 user: Optional[dict] = None):
        
        self.assignment_id = assignment_id
        self.assignment = assignment
        self.course = course
        self.attempt = attempt
        self.body = body
        self.grade = grade
        self.grade_matches_current_submission = grade_matches_current_submission
        self.html_url = html_url
        self.preview_url = preview_url
        self.score = score
        self.submission_comments = submission_comments
        self.submission_type = submission_type
        self.submitted_at = submitted_at
        self.url = url
        self.user_id = user_id
        self.user = user
        self.grader_id = grader_id
        self.graded_at = graded_at
        self.late = late
        self.assignment_visible = assignment_visible
        self.excused = excused
        self.missing = missing
        self.late_policy_status = late_policy_status
        self.points_deducted = points_deducted
        self.seconds_late = seconds_late
        self.workflow_state = workflow_state
        self.extra_attempts = extra_attempts
        self.anonymous_id = anonymous_id
        self.posted_at = posted_at
        self.read_status = read_status
        self.redo_request = redo_request
    def parse_json_into_submissions(submission_json):
        submissions = []
        for body in submission_json:
            submissions.append(Submission(**body))
        return submissions