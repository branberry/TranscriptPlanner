class Course:
    def __init__(self, id, name, prereqs, offeredIn, description, department):
        self.id = id
        self.name = name
        self.prereqs = prereqs
        self.offeredIn = offeredIn
        self.description = description
        self.department = department
    