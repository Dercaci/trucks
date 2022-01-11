from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine



app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/d42_database'
} 
db = MongoEngine()
db.init_app(app)


class Trucks(db.Document):
    driver_name = db.StringField(required = True, unique= True)
    truck_number = db.StringField(required = True, unique = True)


class TruckApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            truck = Trucks(**body).save()

        except:
            return jsonify({"response": "Error 400 Bad Request"})    
        return jsonify({"response": "201 Created"})
        

    def get(self):
        trucks = Trucks.objects().to_json()
        return Response(trucks)

api.add_resource(TruckApi, '/trucks')

if __name__ == '__main__':
    app.run(debug=True)