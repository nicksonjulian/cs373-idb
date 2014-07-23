from models import Athlete, Events, Country
from serializers.py import AthleteSerializer, EventsSerializer, CountrySerializer

from django.http import http404

from rest_framework.view import APIView
from rest_framework.response import Response

class AthleteList(APIView):
	def get(self, request, format=None):
		athletes = Athlete.object.all()
		serialized_athletes = AthleteSerializer(athletes, many=True)
		return Response(serialized_athletes.data)

class AthleteDetail(APIView):
	def get_object(self, pk):
		try:
			return Athlete.object.get(pk=pk)
		except Athlete.DoesNotExist:
			raise http404

	def get(self, request, pk, format=None):
		athlete = self.get_object(pk)
		serialized_athlete = AthleteSerializer(athlete)
		return Response(serialized_athlete.data)

class EventsList(APIView):
	def get(self, request, format=None):
		events = Events.object.all()
		serialized_events = EventsSerializer(events, many=True)
		return Response(serialized_events.data)

class EventsDetail(APIView):
	def get_object(self, pk):
		try:
			return Events.object.get(pk=pk)
		except Events.DoesNotExist:
			raise http404

	def get(self, request, pk, format=None):
		events = self.get_object(pk)
		serialized_events = EventsSerializer(events)
		return Response(serialized_events.data)


class CountryList(APIView):
	def get(self, request, format=None):
		countries = Country.object.all()
		serialized_countries = CountrySerializer(countries, many=True)
		return Response(serialized_countries.data)

class CountryDetail(APIView):
	def get_object(self, pk):
		try:
			return Country.object.get(pk=pk)
		except Country.DoesNotExist:
			raise http404

	def get(self, request, pk, format=None):
		country = self.get_object(pk)
		serialized_country = CountrySerializer(country)
		return Response(serialized_country.data)