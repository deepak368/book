from django.forms import SelectMultiple

from .models import addbookmodel
import django_filters

class bookFilter(django_filters.FilterSet):

    class Meta:
        model=addbookmodel
        fields=['Book_name']


