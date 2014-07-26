from home.models import Athlete, Country, Events

from rest_framework import serializers

#or use HyperModelSerializer
class AthleteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Athlete
		fields = (
			'id',
			'first_name',
			'last_name',
			'country',
			'gender',
			'birthdate',
			'height',
			'weight',
			'gold_medals',
			'silver_medals',
			'bronze_medals'
		)

class EventsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Events
		fields = (
			'id',
			'name',
			'sport',
			'desc',
			'gold_medalists',
			'silver_medalists',
			'bronze_medalists'
		)

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = (
			'id',
			'name',
			'description',
			'total_gold_medals',
			'total_silver_medals',
			'total_bronze_medals',
			'athletes'
		)