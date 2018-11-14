class Course:
    def __init__(self, id, name, credits, prereqs, courseNum,  offeredIn, description, department):
        self.id = id
        self.name = name
        self.credits = credits
        self.prereqs = prereqs
        self.courseNum = courseNum
        self.offeredIn = offeredIn
        self.description = description
        self.department = department
    