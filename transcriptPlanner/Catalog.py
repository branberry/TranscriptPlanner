import csv
import json
from Course import Course

class Catalog:
    """
        This class contains the list of all of the courses,
        and methods to load and retrieve courses
    """
    def __init__(self, courses=[]):
        self.courses = courses

    def get_course(self, id):
        """
            Finds a course given an integer ID
        """
        id = str(id)
        for i in range(len(self.courses)):
            if self.courses[i].id == id:
                return self.courses[i]
    
    def load_courses(self, file):
        """
            From a CSV file, the catalog is filled with the courses
        """
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.courses.append(Course(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7]))
        self.courses.pop(0)
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)

