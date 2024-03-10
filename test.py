import unittest
from calculator import app

class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
        response = self.app.post('/calculate', data={'num1': '10.9875643211', 'num2': '3', 'operation': 'add'})
        data = response.get_json()
        self.assertEqual(data['result'], 13.9875643211)

    def test_subtraction(self):
        response = self.app.post('/calculate', data={'num1': '2', 'num2': '2.2', 'operation': 'subtract'})
        data = response.get_json()
        self.assertEqual(data['result'], -0.2)

if __name__ == '__main__':
    unittest.main()
