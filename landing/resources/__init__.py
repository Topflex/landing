from flask_restful import Resource, reqparse
from landing.models.subscriptioner import SubscriptionerModel

class SubmitForm(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email', type=str)
  parser.add_argument('name', type=str)

  @classmethod
  def post(cls):
    args = cls.parser.parse_args()
    if SubscriptionerModel.find_by_email(args['email']):
      return {'message': 'Вы уже в списке!'}, 400
    sub = SubscriptionerModel(**args)

    SubscriptionerModel.save_to_db(sub)
    SubscriptionerModel.send_confirmation_email(sub)
    return {'message': 'Спасибо за подписку! Проверяйте почтовый ящик'}, 200
