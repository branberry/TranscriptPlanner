import csv
import json
import ast

from Course import Course
from Degree import Degree
from Transcript import Transcript

class CourseCatalog:
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
    
    def get_course_by_name(self, name):
        """
            find a course by a given short name
        """
        for i in range(len(self.courses)):
            if self.courses[i].courseNum == name:
                return self.courses[i]

    def load_courses(self, file):
        """
            From a CSV file, the catalog is filled with the courses
        """
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.courses.append(Course(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7]))

        # removing the first row because it contains column headers
        self.courses.pop(0)
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)


class DegreeCatalog:

    def __init__(self, degrees=[]):
        self.degrees = degrees

    def load_degrees(self, file):

        with open(file) as json_file:
            data = json_file.read()
            data = ast.literal_eval(data)
            
            for d in data:
                degree = Degree(d,data[d])
                self.degrees.append(degree)

    def get_degree(self, degree_name):
        index = next((index for (index, d) in enumerate(self.degrees) if d.major == degree_name), None)
        return self.degrees[index]
        
    def to_JSON(self):
        return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)

