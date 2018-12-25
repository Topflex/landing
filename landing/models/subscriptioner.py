import os
from flask import request
from landing.db import db
from requests import Response, post
import random

MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM_TITLE = 'tellr beta'
FROM_EMAIL = 'test@tellr.ru'

class SubscriptionerModel(db.Model):
  __tablename__ = 'subscriptioners'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)

  def __init__(self, name, email):
    self.name = name
    self.email = email

  def json(self):
    return {
      'name': self.name,
      'email': self.email
    }

  def send_confirmation_email(self):
    number = random.randint(20, 150)
    return post(
      f'http://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages',
      auth=('api', MAILGUN_API_KEY),
      data={
        'from': f'{FROM_TITLE} <{FROM_EMAIL}>',
        'to': self.email,
        'subject': f'Вы {number} в списке бета-тестеров',
        'text': 'В принципе это всё'
      }
    )

  @classmethod
  def find_by_email(cls, email):
    return cls.query.filter_by(email=email).first()
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
  
  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()