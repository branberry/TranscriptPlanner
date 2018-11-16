import csv
import json
from Course import Course


class Degree:
    def __init__(self, degree_requirements=[]):
        self.degree_requirements = degree_requirements

