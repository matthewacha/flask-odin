"""Import dependencies"""
import unittest
from flask_script import Manager
from app import app

#create an instance of class that will handle our commands
MANAGER = Manager(app)

"""define our command for testing called "test"
Usage: python manage.py test"""
@MANAGER.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@MANAGER.command
def run():
    """Starts the server and debugs with the shell"""
    app.run(debug=True)

if __name__ == '__main__':
    MANAGER.run()
