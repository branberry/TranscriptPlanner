import csv
import json
from Course import Course


class Degree:
    def __init__(self, major, degree_requirements=[]):
        self.degree_requirements = degree_requirements
        self.major = major
    def to_JSON(self):
        return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)