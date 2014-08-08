from django.test import TestCase

from home.models import Athlete, Country, Events

class HomeTests(TestCase):
    fixtures = ['testdata.json']

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

    def test_Athlete_type(self):
        athlete = Athlete(self, "John", "Doe", "US")
        self.assertEqual(athlete.get_cname(), "athlete")

    def test_Athlete_database(self):
        athlete = Athlete.objects.get(first_name="Ireen")
        self.assertEqual(athlete.last_name, "Wust")

    def test_Events1(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.name, "Luge Doubles")

    def test_Events2(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.sport, "Luge")

    def test_Events3(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.desc, "Riding on cars")

    def test_Events_type(self):
        event = Events(self, "Luge Doubles", "Luge", "Riding on cars")
        self.assertEqual(event.get_cname(), "events")

    def test_Events_database(self):
        event = Events.objects.get(name="Luge Doubles")
        self.assertEqual(event.sport, "Luge")

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

    def test_Country_type(self):
        country = Country(self, "Egypt", "Made of sand")
        self.assertEqual(country.get_cname(), "country")

    def test_Country_database(self):
        country = Country.objects.get(name="Germany")
        self.assertEqual(country.country_code, "ger")

    def test_Athlete_Country_link(self):
        athlete = Athlete.objects.get(first_name="Ireen")
        country = athlete.country
        self.assertEqual(country.name, "Netherlands")
