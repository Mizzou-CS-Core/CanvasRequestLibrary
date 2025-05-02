from typing import Optional


class Submission:
    def __init__(self,
                 canvas_id: int,
                 body: Optional[str],
                 url: Optional[str],
                 grade: str,
                 score: float,
                 submitted_at: Optional[str],
                 assignment_id: int,
                 user_id: int,
                 submission_type: Optional[str],
                 workflow_state: str,
                 grade_matches_current_submission: bool,
                 graded_at: str,
                 grader_id: int,
                 attempt: Optional[int],
                 cached_due_date: Optional[str],
                 excused: bool,
                 late_policy_status: Optional[str],
                 points_deducted: Optional[float],
                 grading_period_id: Optional[int],
                 extra_attempts: Optional[int],
                 posted_at: Optional[str],
                 redo_request: bool,
                 custom_grade_status_id: Optional[int],
                 sticker: Optional[str],
                 late: bool,
                 missing: bool,
                 seconds_late: int,
                 entered_grade: str,
                 entered_score: float,
                 preview_url: Optional[str]):
        self.id = canvas_id
        self.body = body
        self.url = url
        self.grade = grade
        self.score = score
        self.submitted_at = submitted_at
        self.assignment_id = assignment_id
        self.user_id = user_id
        self.submission_type = submission_type
        self.workflow_state = workflow_state
        self.grade_matches_current_submission = grade_matches_current_submission
        self.graded_at = graded_at
        self.grader_id = grader_id
        self.attempt = attempt
        self.cached_due_date = cached_due_date
        self.excused = excused
        self.late_policy_status = late_policy_status
        self.points_deducted = points_deducted
        self.grading_period_id = grading_period_id
        self.extra_attempts = extra_attempts
        self.posted_at = posted_at
        self.redo_request = redo_request
        self.custom_grade_status_id = custom_grade_status_id
        self.sticker = sticker
        self.late = late
        self.missing = missing
        self.seconds_late = seconds_late
        self.entered_grade = entered_grade
        self.entered_score = entered_score
        self.preview_url = preview_url

    @staticmethod
    def parse_json_into_submissions(submission_json):
        submissions = []
        for body in submission_json:
            submissions.append(Submission(**body))
        return submissions
