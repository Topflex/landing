"""
BaseTest

Должен быть родительским классом всех не-юнит тестов.
Позволяет создать новый инстанс БД и тестировать на чистой базе.

"""

from unittest import TestCase
from landing import app
from landing.db import db

class BaseTest(TestCase):
  def setUp(self):
    # runs before every test
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    # context manager
    with app.app_context():
      # loads all the app variables and config and lets us mimic as the app is working
      db.init_app(app)
      db.create_all()
      # get a test client
      self.app = app.test_client()
      # allows us to access the app context later
      self.app_context = app.app_context

  def tearDown(self):
    # runs after every test
    with app.app_context():
      # a simple cleanup
      db.session.remove()
      db.drop_all()