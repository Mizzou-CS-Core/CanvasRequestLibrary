class Group:
    def __init__(self, name: str, canvas_id: int, members_count: int, course_id: int):
        self.name = name
        self.id = canvas_id
        self.members_count = members_count
        self.courses = course_id

    @staticmethod
    def parse_groups_from_json(groups_json) -> []:
        groups = []
        for body in groups_json:
            groups.append(Group(name=body['name'], canvas_id=body['id'], members_count=body['members_count'],
                                course_id=body['course_id']))
        return groups
