import datetime
from haystack import indexes
from home.models import Athlete, Country, Events

class AthleteIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	content_auto = indexes.EdgeNgramField(model_attr='first_name')
	content_auto2 = indexes.EdgeNgramField(model_attr='last_name')

	def get_model(self):
		return Athlete

	def index_queryset(self, using=None):
		#used when entired index for model is updated
		return self.get_model().objects.all()

	def prepare(self, obj):
		self.prepared_data = super(AthleteIndex, self).prepare(obj)
		self.prepareD_data['text'] = obj.last_name
		return self.prepared_data