class Person:
    def __init__(self, name: str, login_id: str, canvas_id: int, sortable_name: str):
        self.name = name
        self.login_id = login_id
        self.canvas_id = canvas_id
        self.sortable_name = sortable_name
    @staticmethod
    def parse_people_from_json(people_json) -> []:
        people = []
        for body in people_json:
            people.append(Person(name=body['name'], canvas_id=body['id'], login_id=body['login_id'], sortable_name=body['sortable_name']))
        return people