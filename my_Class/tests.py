from django.test import TestCase, SimpleTestCase

<<<<<<< HEAD

class SimpleTest(SimpleTestCase):
   def test_home_page_status(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)
=======
# Create your tests here.
class SimpleTest(SimpleTestCase):
   def test_home_page_status(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)
>>>>>>> 43975bd1f535576c394350041ce441a5701a04bf
