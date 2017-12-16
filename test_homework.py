import unittest
from nokia_homework import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_response_type(self):
        r = self.app.get('/')

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
