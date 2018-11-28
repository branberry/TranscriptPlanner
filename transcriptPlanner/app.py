from flask import Flask, json,jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
from Course import Course
from Degree import Degree
from Catalog import CourseCatalog, DegreeCatalog
from Transcript import Transcript

import json
import ast

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('transcript')

course_catalog = CourseCatalog()
course_catalog.load_courses('coursecatalog.csv')


degree_catalog = DegreeCatalog()
degree_catalog.load_degrees('degrees.json')

test_transcript = Transcript('ComputerScienceBA')
test_transcript.load_transcript('transcriptExample.json')


test_degree = degree_catalog.get_degree('ComputerScienceBA')

test_transcript.reccommend(degree_catalog)       

#print(test_transcript.audit_transcript(degree_catalog.get_degree('Manangement Information System Major')))

#print(res)
class HelloWorld(Resource):
    """
        Test REST Endpoint
    """
    def get(self):
        return {'hello': 'world'}

class CourseCatalogResource(Resource):
    """
        This API resource provides course catalog data to the user
    """
    def get(self):
        return course_catalog.to_JSON()

class DegreeCatalogResource(Resource):
    """
        This API resource provides degree catalog data to the user     
    """
    def get(self):
        return degree_catalog.to_JSON()
class TranscriptResource(Resource):
    """
        This API endpoint handles the transcript being sent to and from the frontend
    """

    def post(self):
        """
            This method handles a post request to audit a transcript
        """
        args = parser.parse_args()

        data = ast.literal_eval(args['transcript'])

        transcript = Transcript(data['major'],data['courses'])

        degree = degree_catalog.get_degree(data['major'])

        result = {}

        audit = transcript.audit_transcript(degree)

        result['audit'] = audit

        reccommendations = transcript.reccommend(degree_catalog)

        result['reccommendations'] = reccommendations

        return result, 201


api.add_resource(HelloWorld, '/')
api.add_resource(CourseCatalogResource, '/coursecatalog')
api.add_resource(DegreeCatalogResource, '/degreecatalog')
api.add_resource(TranscriptResource,'/transcript')

if __name__ == '__main__':
    app.run(debug=True)