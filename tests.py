from django.test import TestCase

from home.models import Athlete, Country, Events

class HomeTests(TestCase):

    def test_Athlete1(self):
        athlete = Athlete(self,"John", "Doe", "US")
        self.assertEqual(athlete.first_name, "John")

    def test_Athlete2(self):
        athlete = Athlete(self, "John", "Doe", "US")
        self.assertEqual(athlete.last_name, "Doe")

    def test_Athlete3(self):
        #Have to use get_or_create to make the country object to be passed to athlete
        country, created = Country.objects.get_or_create(name="Egypt", description="Made of sand")
        athlete = Athlete(self, "John", "Doe", country.id)
        self.assertEqual(athlete.country.name, "Egypt")

    def test_Events1(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.name, "Luge Doubles")

    def test_Events2(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.sport, "Luge")

    def test_Events3(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.desc, "Riding on cars")

    def test_Country1(self):
        country = Country(self, "Egypt", "Made of sand")
        self.assertEqual(country.name, "Egypt")

    def test_Country2(self):
        country = Country(self, "Egypt", "Made of sand")
        self.assertEqual(country.description, "Made of sand")

    def test_Country3(self):
        country = Country(self, "Egypt", "Made of sand", 10, 2, 8)
        self.assertEqual(country.total_gold_medals, 10)

    def test_Country4(self):
        country = Country(self, "Egypt", "Made of sand", 10, 2, 8)
        self.assertEqual(country.total_bronze_medals, 8)
