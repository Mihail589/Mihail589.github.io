from flask import Flask
import math
#import g4f
from flask_restful import Api, Resource, reqparse
class GPTResponce(Resource):
    def put(self, responce=""):
        parser = reqparse.RequestParser()
        parser.add_argument("Nok")
        params = parser.parse_args()
        data = list(map(int, params["Nok"].split()))

        lcm = math.lcm(*data)
        var = {"NOK =":lcm}
        return var
if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(GPTResponce, "/NOK", "/nok", "/NOK/", "/nok/")
    app.run()
#curl -X PUT -d argument={"Nok": "10 20 50"} http://localhost:8080/nok