from django_filters import CharFilter, DateFromToRangeFilter, FilterSet
from .models import Event


class EventFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    date = DateFromToRangeFilter()
    location = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'organizer']