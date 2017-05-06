# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__) # load config from this file

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',

))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    params = request.form

    # Check test:
    if 'tests' in params.keys():
        return make_response(jsonify(dict(result=True, value='test_route_index')))

    return 'El app funciona'
