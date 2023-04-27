import django_filters
from .models import Houseuploads

class ListingFilter(django_filters.FilterSet):
     class Meta:
        model = Houseuploads
        fields = {'location':
               ['contains'],
               'housetype':
               ['contains'], 
               'rentmonth':
               ['contains']}
