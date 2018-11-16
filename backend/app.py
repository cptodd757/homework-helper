from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

array = [
    {"question": "King James died in ____", "answer": "1620"},
    {"question": "I like ____", "answer": "pizza"},
    {"question": "Nico is ___", "answer": "cool"},
    {"question": "Cata ___", "answer": "lit"},
    {"question": "Reading from the ___", "answer": "server"},
]

class Getter(Resource):
    def get(self):
        return array;
        
class Poster(Resource): 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("string")
        args = parser.parse_args()
        test = args["string"].split()
        answer = test[0]
        test[0] = "___"
        newThing = " ".join(test)
        obj = {"question": newThing, "answer": answer}
        array.append(obj)
        return obj
        
api.add_resource(Getter, "/get")
api.add_resource(Poster, "/post")
app.run(debug=True)
