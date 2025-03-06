import unittest
import json
from app import app


class TestMLApp(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_health_endpoint(self):
        response = self.app.get('/health')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')


    def test_predict_endpoint(self):
        # Sample Iris features (Setosa)
        test_features = [5.1, 3.5, 1.4, 0.2]
        response = self.app.post('/predict',
                                 data=json.dumps({'features': test_features}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', data)
        self.assertIn('class', data)


if __name__ == '__main__':
    unittest.main()
