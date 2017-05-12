from flask import Flask
from flask_restful import Api
from support import database
from support import firebase


app = Flask(__name__)
api = Api(app)

db = database.Database()


if '__main__' == __name__:
    app.run(host='0.0.0.0', port=80)
