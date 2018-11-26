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


test_degree = degree_catalog.get_degree('ComputerScienceBA')

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
        args = parser.parse_args()
        print(args['transcript'])

        data = ast.literal_eval(args['transcript'])

        transcript = Transcript(data['major'],data['courses'])

        degree = degree_catalog.get_degree(data['major'])

        print(degree)
        result = transcript.audit_transcript(degree)

        print(result)

        return result, 201


api.add_resource(HelloWorld, '/')
api.add_resource(CourseCatalogResource, '/coursecatalog')
api.add_resource(DegreeCatalogResource, '/degreecatalog')
api.add_resource(TranscriptResource,'/transcript')

if __name__ == '__main__':
    app.run(debug=True)