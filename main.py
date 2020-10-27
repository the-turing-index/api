from flask import Flask
from flask_restful import Resource, Api
from data.calendar_json import calendars

app = Flask(__name__)
api = Api(app)

class Calendars(Resource):
    def get(self):
        return calendars

api.add_resource(Calendars, '/calendars')

if __name__ == '__main__':
    app.run(debug=False)
