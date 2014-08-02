from home.models import Athlete, Events, Country
from api.serializer import AthleteSerializer, EventsSerializer, CountrySerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class AthleteList(APIView):
	def get(self, request, format=None):
		athletes = Athlete.objects.all()
		serialized_athletes = AthleteSerializer(athletes, many=True)
		return Response(serialized_athletes.data)

class AthleteDetail(APIView):
    def get_object(self, pk):
        name = pk.split("_")
        f_name = name[0].capitalize()
        l_name = name[1].capitalize()
        try:
            return Athlete.objects.get(first_name = f_name)
        except Athlete.DoesNotExist:
            raise Http404

    def get_object_num(self, pk):
        try:
            return Athlete.objects.get(pk = pk)
        except Athlete.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if (pk.isnumeric()):
            athlete = self.get_object_num(pk)
        else:
            athlete = self.get_object(pk)
        serialized_athlete = AthleteSerializer(athlete)
        return Response(serialized_athlete.data)

class EventsList(APIView):
	def get(self, request, format=None):
		events = Events.objects.all()
		serialized_events = EventsSerializer(events, many=True)
		return Response(serialized_events.data)

class EventsDetail(APIView):
    def get_object(self, name):
        try:
            event_name = name.replace("_", " ").title()
            event_name = event_name.replace("ies", "ies'").replace("ns", "n's")
            return Events.objects.get(name = event_name)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, sport_name, event_name, format=None):
        event = self.get_object(event_name)
        serialized_event = EventsSerializer(event)
        return Response(serialized_event.data)

class EventsDetailPK(APIView):
    def get_object(self, pk):
        try:
            return Events.objects.get(pk = pk)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serialized_event = EventsSerializer(event)
        return Response(serialized_event.data)

class CountryList(APIView):
	def get(self, request, format=None):
		countries = Country.objects.all()
		serialized_countries = CountrySerializer(countries, many=True)
		return Response(serialized_countries.data)

class CountryDetail(APIView):
    def get_object(self, pk):
        try:
            country_name = pk.replace("_", " ").title()
            return Country.objects.get(name = country_name)
        except Country.DoesNotExist:
            raise Http404

    def get_object_num(self, pk):
        try:
            return Country.objects.get(pk = pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if (pk.isnumeric()):
            country = self.get_object_num(pk)
        else:
            country = self.get_object(pk)
        serialized_country = CountrySerializer(country)
        return Response(serialized_country.data)