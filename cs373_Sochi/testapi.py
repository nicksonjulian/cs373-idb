from django.test import TestCase
from django.test.client import Client

class APITestCase(TestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.client = Client()

    def test_api_athlete(self):
        response = self.client.get('/api/athlete/4/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "Victor")
        self.assertEqual(response.data["last_name"], "An")

    def test_api_county(self):
        response = self.client.get('/api/country/3/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Netherlands")

    def test_api_event(self):
        response = self.client.get('/api/event/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Ice Dance Free Dance")
        self.assertEqual(response.data["sport"], "Figure Skating")

    def test_api_athlete_name(self):
        response = self.client.get('/api/athlete/victor_an/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "Victor")
        self.assertEqual(response.data["last_name"], "An")

    def test_api_county_name(self):
        response = self.client.get('/api/country/netherlands/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Netherlands")

    def test_api_event_name(self):
        response = self.client.get('/api/event/figure_skating-ice_dance_free_dance/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Ice Dance Free Dance")
        self.assertEqual(response.data["sport"], "Figure Skating")
