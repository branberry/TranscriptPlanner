import csv
import json
from Course import Course


class Transcript:
    """
        This class will take a catalog of courses, and read them into an array.
        This course will use an Auditor object to handle the auditing of the transcript's courses
        with respect to a given degree.
        Will contain list of courses as well as total credits
    """
    def __init__(self, courses=[]):
        self.courses = courses
        self.credits_total = 0;
		self.Difference =
    """
        will take the courses[] built from Transcript.json 
        file and sum up the credits
        :returns integer sum total of the credits
         associated with each courses in the list
    """
    def sum_credits_in_transcript(self, courses):
        for Course in courses:
            self.credits_total = self.credits_total + Course.credit
        
	
    """
        this will take two parameters, namely the (Degrees.json and 
        Transcript in the form of courses[]) 
        it'll build a list of courses that are the 
        difference between the transcript and requirement
    """
    """def auditor(self):(self, courses, Degrees):"""
			possibly return
			return difference (between transcript and degree[course ID,...]
			




