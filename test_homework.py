"""
Tests for nokia homework
"""
import unittest
from nokia_homework import APP


class MyTestCase(unittest.TestCase):
    """
    Main test case
    """
    def setUp(self):
        APP.testing = True
        self.app = APP.test_client()

    def test_response_type(self):
        """
        Tests if response is a json
        :return: None
        """
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
