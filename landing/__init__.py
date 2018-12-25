from flask import Flask, render_template
from flask_restful import Api
from landing.db import db
from dotenv import load_dotenv
from pathlib import Path
import os
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

env_path = Path('landing') / '.env'
load_dotenv(dotenv_path=env_path)

@app.before_first_request
def create_tables():
  db.create_all()

from landing import routes
from landing.resources import SubmitForm

api.add_resource(SubmitForm, '/form')

