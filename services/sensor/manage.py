# users-service/manage.py

import unittest
from flask.cli import FlaskGroup

from project import create_app, sensor

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command()
def start_ss():
	sensor.begin()


if __name__ == '__main__':
    cli()