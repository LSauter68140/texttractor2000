
from task7_api import getTranslation
from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__) 
api = Api(app)
class Translate(Resource):
    def post(self):
        try:
            data = request.get_json()
        except:
            return {'errorMessage': 'Wrong request...'}, 500
        if(len(data)>0):
            response = getTranslation(data)
            err = None
        else:
            return {'errorMessage': 'Please, provide a fileName...'}, 500
        if response:
            return response, 200
        else:
            return {'errorMessage': err}, 404
        
        
api.add_resource(Translate, '/translate') 
if __name__ == "__main__":
    app.run()

    

## input

## language
## output in text or audio
## text or image 
## femal or mal if audio