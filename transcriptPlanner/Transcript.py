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
        response = []
        if degree.major == self.major:
            for i in range(len(degree.degree_requirements)):
                response.append({})
                response[i]['completed'] = 0
                response[i]['diff'] = []
                print(response)
                for j in range(len(degree.degree_requirements[i]['courses'])):
                    if degree.degree_requirements[i]['courses'][j] in self.courses:
                        print(self.courses[j])
                        response[i]['completed'] += 1
                    else:
                        response[i]['diff'].append(degree.degree_requirements[i]['courses'][j])

                response[i]['requirement_met'] = (response[i]['completed'] >= degree.degree_requirements[i]['required'])
                                                   
        else:
            print('You are not majoring in ' + degree.major +", you are majoring in " + self.major)
        print(response)
        return response

    def load_transcript(self, file):

        with open(file) as json_file:
            data = json_file.read()
            data = ast.literal_eval(data)
            self.courses = data['courses']
            self.major = data['major']
            print(self.courses)


t = Transcript('Computer Science')

d = Degree('Computer Science')