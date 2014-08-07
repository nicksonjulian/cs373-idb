from haystack import indexes
from home.models import Events


class EventsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    sport = indexes.CharField(model_attr='sport')
    desc = indexes.CharField(model_attr='desc')

    def get_model(self):
        return Events

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()