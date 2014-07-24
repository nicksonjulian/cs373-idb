from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Athlete, Country, Events

class AthleteResource(ModelResource):
	class Meta:
		queryset = Athlete.objects.all()
		resource_name = 'athlete'
		filtering = {"first_name" : ALL}

class CountryResource(ModelResource):
	class Meta:
		queryset = Country.objects.all()
		resource_name = 'country'
		filtering = {"name" : ALL}

class EventResource(ModelResource):
	class Meta:
		queryset = Events.objects.all()
		resource_name = 'event'
		filtering = {"name" : ALL}
