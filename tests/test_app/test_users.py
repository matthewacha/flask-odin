"""import dependencies"""
import unittest
from app import APP

class TestUsers(unittest.TestCase):
    """sets up and tears down environment before and after each test suite"""
    def setUp(self):
        self.tester = APP.test_client(self)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
