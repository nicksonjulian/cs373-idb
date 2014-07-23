from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Athlete, Country, Events

class AthleteResource(ModelResource):
	class Meta:
		queryset = Athlete.objects.all()
		resource_name = 'athlete'
		fitering = {"first_name" : ALL}

class CountryResource(ModelResource):
	class Meta:
		queryset = Country.objects.all()
		resource_name = 'country'
		fitering = {"name" : ALL}

class EventResource(ModelResource):
	class Meta:
		queryset = Events.objects.all()
		resource_name = 'event'
		fitering = {"name" : ALL}
