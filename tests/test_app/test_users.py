"""import dependencies"""
import unittest
from app import app

class TestUsers(unittest.TestCase):
    """sets up and tears down environment before and after each test suite"""
    def setUp(self):
        self.tester = app.test_client(self)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
