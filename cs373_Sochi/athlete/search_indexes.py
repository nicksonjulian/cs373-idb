from haystack import indexes
from home.models import Athlete


class AthleteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    f_name = indexes.CharField(model_attr='first_name')
    l_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Athlete

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()