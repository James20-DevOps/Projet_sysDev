import unittest
import json
from app import app

class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        # Créer un client de test Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_students(self):
        response = self.app.get('/pozos/api/v1.0/get_student_ages')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('student_ages', data)
        self.assertIsInstance(data['student_ages'], dict)

    def test_get_student_age_not_found(self):
        response = self.app.get('/pozos/api/v1.0/get_student_ages/unknown_student')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Not found')

if __name__ == '__main__':
    unittest.main()
