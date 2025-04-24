class Group:
    def __init__(self, name: str, id: int, members_count: int):
        self.name = name
        self.id = id
        self.members_count = members_count
    @staticmethod
    def parse_groups_from_json(groups_json) -> []:
        groups = []
        for body in groups_json:
            groups.append(Group(name=body['name'], id=body['id'], members_count=body['members_count']))
        return groups

