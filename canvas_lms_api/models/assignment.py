class Assignment:
    def __init__(self, id, name, description, created_at, updated_at, due_at=None, lock_at=None, unlock_at=None,
                 has_overrides=False, all_dates=None, course_id=None, html_url=None, submissions_download_url=None,
                 assignment_group_id=None, due_date_required=False, allowed_extensions=None, max_name_length=255,
                 turnitin_enabled=False, vericite_enabled=False, turnitin_settings=None,
                 grade_group_students_individually=False,
                 external_tool_tag_attributes=None, peer_reviews=False, automatic_peer_reviews=False,
                 peer_review_count=0,
                 peer_reviews_assign_at=None, intra_group_peer_reviews=False, group_category_id=None,
                 needs_grading_count=0,
                 needs_grading_count_by_section=None, position=0, post_to_sis=False, integration_id=None,
                 integration_data=None,
                 points_possible=0, submission_types=None, has_submitted_submissions=False, grading_type=None,
                 grading_standard_id=None,
                 published=False, unpublishable=False, only_visible_to_overrides=False, locked_for_user=False,
                 lock_info=None,
                 lock_explanation=None, quiz_id=None, anonymous_submissions=False, discussion_topic=None,
                 freeze_on_copy=False,
                 frozen=False, frozen_attributes=None, submission=None, use_rubric_for_grading=False,
                 rubric_settings=None,
                 rubric=None, assignment_visibility=None, overrides=None, omit_from_final_grade=False,
                 hide_in_gradebook=False,
                 moderated_grading=False, grader_count=0, final_grader_id=None, grader_comments_visible_to_graders=True,
                 graders_anonymous_to_graders=False, grader_names_visible_to_final_grader=True, anonymous_grading=False,
                 allowed_attempts=-1, post_manually=False, score_statistics=None, can_submit=False, ab_guid=None,
                 annotatable_attachment_id=None, anonymize_students=False, require_lockdown_browser=False,
                 important_dates=False,
                 muted=False, anonymous_peer_reviews=False, anonymous_instructor_annotations=False,
                 graded_submissions_exist=False,
                 is_quiz_assignment=False, in_closed_grading_period=False, can_duplicate=False, original_course_id=None,
                 original_assignment_id=None, original_lti_resource_link_id=None, original_assignment_name=None,
                 original_quiz_id=None,
                 workflow_state=None, secure_params=None, lti_context_id=None, visible_to_everyone=False,
                 restrict_quantitative_data=False, free_form_criterion_comments=False):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.due_at = due_at
        self.lock_at = lock_at
        self.unlock_at = unlock_at
        self.has_overrides = has_overrides
        self.all_dates = all_dates
        self.course_id = course_id
        self.html_url = html_url
        self.submissions_download_url = submissions_download_url
        self.assignment_group_id = assignment_group_id
        self.due_date_required = due_date_required
        self.allowed_extensions = allowed_extensions
        self.max_name_length = max_name_length
        self.turnitin_enabled = turnitin_enabled
        self.vericite_enabled = vericite_enabled
        self.turnitin_settings = turnitin_settings
        self.grade_group_students_individually = grade_group_students_individually
        self.external_tool_tag_attributes = external_tool_tag_attributes
        self.peer_reviews = peer_reviews
        self.automatic_peer_reviews = automatic_peer_reviews
        self.peer_review_count = peer_review_count
        self.peer_reviews_assign_at = peer_reviews_assign_at
        self.intra_group_peer_reviews = intra_group_peer_reviews
        self.group_category_id = group_category_id
        self.needs_grading_count = needs_grading_count
        self.needs_grading_count_by_section = needs_grading_count_by_section
        self.position = position
        self.post_to_sis = post_to_sis
        self.integration_id = integration_id
        self.integration_data = integration_data
        self.points_possible = points_possible
        self.submission_types = submission_types
        self.has_submitted_submissions = has_submitted_submissions
        self.grading_type = grading_type
        self.grading_standard_id = grading_standard_id
        self.published = published
        self.unpublishable = unpublishable
        self.only_visible_to_overrides = only_visible_to_overrides
        self.locked_for_user = locked_for_user
        self.lock_info = lock_info
        self.lock_explanation = lock_explanation
        self.quiz_id = quiz_id
        self.anonymous_submissions = anonymous_submissions
        self.discussion_topic = discussion_topic
        self.freeze_on_copy = freeze_on_copy
        self.frozen = frozen
        self.frozen_attributes = frozen_attributes
        self.submission = submission
        self.use_rubric_for_grading = use_rubric_for_grading
        self.rubric_settings = rubric_settings
        self.rubric = rubric
        self.assignment_visibility = assignment_visibility
        self.overrides = overrides
        self.omit_from_final_grade = omit_from_final_grade
        self.hide_in_gradebook = hide_in_gradebook
        self.moderated_grading = moderated_grading
        self.grader_count = grader_count
        self.final_grader_id = final_grader_id
        self.grader_comments_visible_to_graders = grader_comments_visible_to_graders
        self.graders_anonymous_to_graders = graders_anonymous_to_graders
        self.grader_names_visible_to_final_grader = grader_names_visible_to_final_grader
        self.anonymous_grading = anonymous_grading
        self.allowed_attempts = allowed_attempts
        self.post_manually = post_manually
        self.score_statistics = score_statistics
        self.can_submit = can_submit
        self.ab_guid = ab_guid
        self.annotatable_attachment_id = annotatable_attachment_id
        self.anonymize_students = anonymize_students
        self.require_lockdown_browser = require_lockdown_browser
        self.important_dates = important_dates
        self.muted = muted
        self.anonymous_peer_reviews = anonymous_peer_reviews
        self.anonymous_instructor_annotations = anonymous_instructor_annotations
        self.graded_submissions_exist = graded_submissions_exist
        self.is_quiz_assignment = is_quiz_assignment
        self.in_closed_grading_period = in_closed_grading_period
        self.can_duplicate = can_duplicate
        self.original_course_id = original_course_id
        self.original_assignment_id = original_assignment_id
        self.original_lti_resource_link_id = original_lti_resource_link_id
        self.original_assignment_name = original_assignment_name
        self.original_quiz_id = original_quiz_id
        self.workflow_state = workflow_state
        self.secure_params = secure_params
        self.lti_context_id = lti_context_id
        self.visible_to_everyone = visible_to_everyone
        self.restrict_quantitative_data = restrict_quantitative_data
        self.free_form_criterion_comments = free_form_criterion_comments

    @staticmethod
    def parse_json_into_assignments(assignment_json):
        assignments = []
        for body in assignment_json:
            assignments.append(Assignment(**body))
        return assignments
