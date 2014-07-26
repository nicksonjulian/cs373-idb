from home.models import Athlete, Events, Country
from serializers.py import AthleteSerializer, EventsSerializer, CountrySerializer

from django.http import http404

from rest_framework.view import APIView
from rest_framework.response import Response

#all athletes
def athletes_get(request, format=None):
	athletes = Athlete.object.all()
	serialized_athletes = AthleteSerializer(athletes, many=True)
	return Response(serialized_athletes.data)

def detail(request, athlete_id):
    name = athlete_id.split("_")
    f_name = name[0].capitalize()
    l_name = name[1].capitalize()

    try:
        athlete = Athlete.objects.get(first_name=f_name)
        context = {'athlete': athlete}
    except Athlete.DoesNotExist:
        raise Http404

#Athlete
def athlete_get(request, pk):
    name = athlete_id.split("_")
    f_name = name[0].capitalize()
    l_name = name[1].capitalize()
    try:
        athlete = Athlete.objects.get(first_name=pk)
    except Athlete.DoesNotExist:
        raise Http404
    seriaized_athlete = AthleteSerializer(athlete)
    return Response(serialized_athlete.data)

    #try:
	#    athlete = Athlete.objects.get(first_name=pk)
	#    context = {'athlete': athlete}
	#except Athlete.DoesNotExist:
	#    raise Http404
	#serialized_athlete = AthleteSerializer(athlete)
	#return Response(serialized_athlete.data)

#All Events
def events_get(request, format=None):
	events = Events.object.all()
	serialized_events = EventsSerializer(events, many=True)
	return Response(serialized_events.data)

#Event
def event_get(request, sport, pk, format=None):
    try:
	    #pk = pk.capitalize()
		events = Events.object.get(name=pk.capitalize())
	except Events.DoesNotExist:
		raise http404
	serialized_events = EventsSerializer(events)
	return Response(serialized_events.data)

#All Countries
def countries_get(request, format=None):
	countries = Country.object.all()
	serialized_countries = CountrySerializer(countries, many=True)
	return Response(serialized_countries.data)

#Country
def country_get(request, pk, format=None):
    try:
		country = Country.object.get(pk=pk)
	except Country.DoesNotExist:
		raise http404
	country = get_country_object(pk)
	serialized_country = CountrySerializer(country)
	return Response(serialized_country.data)