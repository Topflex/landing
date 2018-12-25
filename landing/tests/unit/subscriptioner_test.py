from unittest import TestCase
from landing.models.subscriptioner import SubscriptionerModel

class SubTest(TestCase):
  def test_create_sub(self):
    sub = SubscriptionerModel('Андрэ', 'andre@andre.com')
    self.assertEqual(sub.name, 'Андрэ')
    self.assertEqual(sub.email, 'andre@andre.com')
  
  def test_sub_json(self):
    sub = SubscriptionerModel('Андрэ', 'andre@andre.com')
    expected = {
      'name': 'Андрэ',
      'email': 'andre@andre.com'
    }

    self.assertEqual(sub.json(), expected)