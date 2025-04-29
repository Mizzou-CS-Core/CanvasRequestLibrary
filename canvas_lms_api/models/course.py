from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class Calendar:
    ics: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Calendar":
        return cls(ics=data["ics"])


@dataclass
class BlueprintRestrictions:
    content: bool
    points: bool
    due_dates: bool
    availability_dates: bool

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "BlueprintRestrictions":
        return cls(
            content=data["content"],
            points=data["points"],
            due_dates=data["due_dates"],
            availability_dates=data["availability_dates"],
        )


@dataclass
class Course:
    # --- always present ---
    id: int
    name: str
    uuid: str
    workflow_state: str
    account_id: int
    root_account_id: int
    enrollment_term_id: int
    grading_standard_id: int
    license: str
    created_at: str
    default_view: str
    time_zone: str
    apply_assignment_group_weights: bool
    hide_final_grades: bool
    is_public: bool
    is_public_to_auth_users: bool
    public_syllabus: bool
    public_syllabus_to_auth: bool
    storage_quota_mb: int

    # --- optional / permission-gated / include[]=… ---
    sis_course_id:          Optional[str]            = None
    integration_id:         Optional[str]            = None
    sis_import_id:          Optional[int]            = None
    original_name:          Optional[str]            = None
    course_code:            Optional[str]            = None
    grading_periods:        Optional[List[dict]]     = None
    grade_passback_setting: Optional[str]            = None
    start_at:               Optional[str]            = None
    end_at:                 Optional[str]            = None
    locale:                 Optional[str]            = None
    enrollments:            Optional[List[dict]]     = None
    total_students:         Optional[int]            = None
    calendar:               Optional[Calendar]       = None
    syllabus_body:          Optional[str]            = None
    needs_grading_count:    Optional[int]            = None
    term:                   Optional[dict]           = None
    course_progress:        Optional[dict]           = None
    permissions:            Optional[Dict[str,bool]]  = None
    public_description:     Optional[str]            = None
    storage_quota_used_mb:  Optional[int]            = None
    allow_student_assignment_edits:   Optional[bool] = None
    allow_wiki_comments:               Optional[bool] = None
    allow_student_forum_attachments:   Optional[bool] = None
    open_enrollment:                   Optional[bool] = None
    self_enrollment:                   Optional[bool] = None
    restrict_enrollments_to_course_dates: Optional[bool] = None
    course_format:                     Optional[str]  = None
    access_restricted_by_date:         Optional[bool] = None
    blueprint:                         Optional[bool] = None
    blueprint_restrictions:            Optional[BlueprintRestrictions] = None
    blueprint_restrictions_by_object_type: Optional[Dict[str, BlueprintRestrictions]] = None
    template:                          Optional[bool] = None

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Course":
        return cls(
            # always present
            id=data["id"],
            name=data["name"],
            uuid=data["uuid"],
            workflow_state=data["workflow_state"],
            account_id=data["account_id"],
            root_account_id=data["root_account_id"],
            enrollment_term_id=data["enrollment_term_id"],
            grading_standard_id=data["grading_standard_id"],
            license=data["license"],
            created_at=data["created_at"],
            default_view=data["default_view"],
            time_zone=data["time_zone"],
            apply_assignment_group_weights=data["apply_assignment_group_weights"],
            hide_final_grades=data["hide_final_grades"],
            is_public=data["is_public"],
            is_public_to_auth_users=data["is_public_to_auth_users"],
            public_syllabus=data["public_syllabus"],
            public_syllabus_to_auth=data["public_syllabus_to_auth"],
            storage_quota_mb=data["storage_quota_mb"],

            # optional / permission-gated
            sis_course_id=data.get("sis_course_id"),
            integration_id=data.get("integration_id"),
            sis_import_id=data.get("sis_import_id"),
            original_name=data.get("original_name"),
            course_code=data.get("course_code"),
            grading_periods=data.get("grading_periods"),
            grade_passback_setting=data.get("grade_passback_setting"),
            start_at=data.get("start_at"),
            end_at=data.get("end_at"),
            locale=data.get("locale"),
            enrollments=data.get("enrollments"),
            total_students=data.get("total_students"),
            calendar=Calendar.from_json(data["calendar"]) if data.get("calendar") else None,
            syllabus_body=data.get("syllabus_body"),
            needs_grading_count=data.get("needs_grading_count"),
            term=data.get("term"),
            course_progress=data.get("course_progress"),
            permissions=data.get("permissions"),
            public_description=data.get("public_description"),
            storage_quota_used_mb=data.get("storage_quota_used_mb"),
            allow_student_assignment_edits=data.get("allow_student_assignment_edits"),
            allow_wiki_comments=data.get("allow_wiki_comments"),
            allow_student_forum_attachments=data.get("allow_student_forum_attachments"),
            open_enrollment=data.get("open_enrollment"),
            self_enrollment=data.get("self_enrollment"),
            restrict_enrollments_to_course_dates=data.get("restrict_enrollments_to_course_dates"),
            course_format=data.get("course_format"),
            access_restricted_by_date=data.get("access_restricted_by_date"),
            blueprint=data.get("blueprint"),
            blueprint_restrictions=(
                BlueprintRestrictions.from_json(data["blueprint_restrictions"])
                if data.get("blueprint_restrictions") else None
            ),
            blueprint_restrictions_by_object_type=(
                {k: BlueprintRestrictions.from_json(v)
                 for k, v in data["blueprint_restrictions_by_object_type"].items()}
                if data.get("blueprint_restrictions_by_object_type") else None
            ),
            template=data.get("template"),
        )
