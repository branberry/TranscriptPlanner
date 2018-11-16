from flask import Flask, json,jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from Course import Course
from Degree import Degree
from Catalog import Catalog
from Transcript import Transcript

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


catalog = Catalog()
catalog.load_courses('coursecatalog.csv')

class HelloWorld(Resource):
    """
        Test REST Endpoint
    """
    def get(self):
        return {'hello': 'world'}

class CatalogResource(Resource):
    """
        This API resource provides catalog data to the user.
    """
    def get(self):
        return catalog.to_JSON()

api.add_resource(HelloWorld, '/')
api.add_resource(CatalogResource, '/catalog')

if __name__ == '__main__':
    app.run(debug=True)