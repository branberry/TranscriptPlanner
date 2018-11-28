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
        self.credits_total = 0
    
    def audit_transcript(self,degree):
        """
            This method takes in a degree(list if req courses), 
			and compares it with the transcript (loist of completed courses)
        """
        # contains a list of degree requirement objects
        response = []

        for i in range(len(degree.degree_requirements)):

            # adding an empty dictionary to the response list.
            response.append({})
            
            # taken property contains the number of instances where the transcript has a degree requirement course
            response[i]['taken'] = 0
            
            # this list contains all the original courses for the requirement.  This will be used 
            response[i]['all_courses'] = degree.degree_requirements[i]['courses']
            response[i]['incomplete'] = []
            response[i]['complete'] = []
            for j in range(len(degree.degree_requirements[i]['courses'])):
                if degree.degree_requirements[i]['courses'][j] in self.courses:
                    response[i]['taken'] += 1
                    response[i]['complete'].append(degree.degree_requirements[i]['courses'][j])
                else:
                    response[i]['incomplete'].append(degree.degree_requirements[i]['courses'][j])

            # if the count for the requirement met is greater than or equal to what the degree requires, then we have satisfied the requirement
            response[i]['requirement_met'] = (response[i]['taken'] >= degree.degree_requirements[i]['required'])
            response[i]['name'] = degree.degree_requirements[i]['name']
            response[i]['remaining'] = degree.degree_requirements[i]['required'] - response[i]['taken'] 

        return response

    def reccommend(self, degree_catalog):
        reccommendations = []

        for degree in degree_catalog.degrees:
            if degree.major != self.major:
                requirements = self.audit_transcript(degree)

                completed =  True
                for requirement in requirements:
                    if not requirement['requirement_met']:
                        completed = False
                        break
                if completed:
                    reccommendations.append(degree)



    def load_transcript(self, file):

        with open(file) as json_file:
            data = json_file.read()
            data = ast.literal_eval(data)
            self.courses = data['transcript']['courses']
            self.major = data['transcript']['major']
	
    def sum_credits_in_transcript(self, courses):
        """
        will take the courses[] built from Transcript.json 
        file and sum up the credits
        :returns integer sum total of the credits
        associated with each courses in the list
        """
        for Course in courses:
            self.credits_total = self.credits_total + Course.credit
			

t = Transcript('Computer Science')

d = Degree('Computer Science')