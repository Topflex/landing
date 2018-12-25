from landing.models.subscriptioner import SubscriptionerModel
from landing.tests.base_test import BaseTest

class SubTest(BaseTest):
  def test_crud(self):
    with self.app_context():
      sub = SubscriptionerModel('Андрэ', 'andre@andre.com')
      sub.save_to_db()
      self.assertIsNotNone(SubscriptionerModel.find_by_email('andre@andre.com'))
      sub.delete_from_db()
      self.assertIsNone(SubscriptionerModel.find_by_email('andre@andre.com'))