import os, json
from app import app
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config.from_object('config.DevelopmentConfig')
        self.app = app.test_client()
        # with app.app_context():
        #    app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_route(self):
        rv = self.app.get('/', data=dict(tests=True))
        data = json.loads(rv.data.decode('utf8'))

        self.assertTrue(data['result'])
        self.assertEqual(data['value'], 'test_route_index')

if __name__ == '__main__':
    unittest.main()
