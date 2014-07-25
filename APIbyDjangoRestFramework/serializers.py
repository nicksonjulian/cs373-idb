from models import Athlete, Country, Events

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
			'gold_medals',
			'silver_medals',
			'bronze_medals'
		)

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Athlete
		fields = (
			'id',
			'name',
			'sport',
			'country',
			'desc',
			'gold_medalists',
			'silver_medalists',
			'bronze_medalists'
		)

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Athlete
		fields = (
			'id',
			'name',
			'description',
			'country',
			'total_gold_medals',
			'total_silver_medals',
			'total_bronze_medals',
			'athletes'
		)
