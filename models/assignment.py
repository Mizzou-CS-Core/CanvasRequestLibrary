class Assignment:
    def __init__(self, id, name, description, created_at, updated_at, due_at, lock_at, unlock_at, 
                 has_overrides, all_dates, course_id, html_url, submissions_download_url, 
                 assignment_group_id, due_date_required, allowed_extensions, max_name_length, 
                 turnitin_enabled, vericite_enabled, turnitin_settings, grade_group_students_individually, 
                 external_tool_tag_attributes, peer_reviews, automatic_peer_reviews, peer_review_count, 
                 peer_reviews_assign_at, intra_group_peer_reviews, group_category_id, needs_grading_count, 
                 needs_grading_count_by_section, position, post_to_sis, integration_id, integration_data, 
                 points_possible, submission_types, has_submitted_submissions, grading_type, grading_standard_id, 
                 published, unpublishable, only_visible_to_overrides, locked_for_user, lock_info, lock_explanation, 
                 quiz_id, anonymous_submissions, discussion_topic, freeze_on_copy, frozen, frozen_attributes, 
                 submission, use_rubric_for_grading, rubric_settings, rubric, assignment_visibility, overrides, 
                 omit_from_final_grade, hide_in_gradebook, moderated_grading, grader_count, final_grader_id, 
                 grader_comments_visible_to_graders, graders_anonymous_to_graders, grader_names_visible_to_final_grader, 
                 anonymous_grading, allowed_attempts, post_manually, score_statistics, can_submit, ab_guid, 
                 annotatable_attachment_id, anonymize_students, require_lockdown_browser, important_dates, muted, 
                 anonymous_peer_reviews, anonymous_instructor_annotations, graded_submissions_exist, is_quiz_assignment, 
                 in_closed_grading_period, can_duplicate, original_course_id, original_assignment_id, 
                 original_lti_resource_link_id, original_assignment_name, original_quiz_id, workflow_state):
        
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
    def parse_json_into_assignments(assignment_json):
        assignments = []
        for body in assignment_json:
            assignments.append(Assignment(**body))
        return assignments