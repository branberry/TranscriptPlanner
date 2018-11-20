from Degree import Degree

import json
import ast

class Transcript:
    """
        This class will take a catalog of courses, and read them into an array.
        This course will use an Auditor object to handle the auditing of the transcript's courses
        with respect to a given degree.
    """
    def __init__(self,major, courses=[]):
        self.courses = courses
        self.major = major
    
    def audit_transcript(self,degree):
        if degree.major == self.major:
            for i in range(len(degree.degree_requirements)):
                for k in range(len(self.courses)):
                    for j in range(len(degree.degree_requirements[i]['courses'])):
                        if self.courses[k] == degree.degree_requirements[i]['courses'][j]:
                            print(degree.degree_requirements[i]['courses'][j])
        else:
            print('You are not majoring in ' + degree.major +", you are majoring in " + self.major)

    def load_transcript(self, file):

        with open(file) as json_file:
            data = json_file.read()
            data = ast.literal_eval(data)
            self.courses = data['courses']
            self.major = data['major']
            print(self.courses)


t = Transcript('Computer Science')

d = Degree('Computer Science')