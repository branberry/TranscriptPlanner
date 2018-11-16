
class Transcript:
    """
        This class will take a catalog of courses, and read them into an array.
        This course will use an Auditor object to handle the auditing of the transcript's courses
        with respect to a given degree.
    """
    def __init__(self, courses=[]):
        self.courses = courses