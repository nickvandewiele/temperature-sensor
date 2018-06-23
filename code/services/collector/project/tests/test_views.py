import json
import unittest

from project.tests.base import BaseTestCase

class TestCollectorService(BaseTestCase):
    """Tests for the Collector Service."""

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/collector/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])
    

    def test_collect(self):
        """Ensure collect route behaves correctly."""
        
        with self.client:
            response = self.client.get('/collector')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])