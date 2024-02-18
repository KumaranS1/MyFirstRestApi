from flask import Flask, jsonify, request
from flask_restful import Resource, Api

#Creating flask App
app = Flask(__name__)

#Creating object for app

api = Api(app)

#Creating My first Resource

class HelloWorld(Resource):
    """creating decorators for http methods GET, POST, DELETE, PUT """

    def get(self):
        return jsonify({"MyFirstMessage": "Hello Kumaran"})

    def post(self):
        return jsonify({"status" : "Your new message is poaste"})


#Register resource with corresponding
api.add_resource(HelloWorld, '/helloworld')

if __name__ == '__main__':
    app.run(debug=True)