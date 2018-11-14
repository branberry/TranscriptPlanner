class Catalog:
    def __init__(self, courses=[]):
        self.courses = courses

    def get_course(self, id):
        for i in range(len(self.courses)):
            if self.courses[i].id == id:
                return self.courses[i]