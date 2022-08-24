import django_filters
from .models import Country

class CountryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name",lookup_expr="icontains",label="Name:")
    region = django_filters.CharFilter(field_name="region",lookup_expr="icontains",label="Region:")
    subregion = django_filters.CharFilter(field_name="subregion",lookup_expr="icontains",label="Subregion:")
    class Meta:
        model = Country
        fields = ["name","region","subregion","user"]
    def __init__(self,*args,**kwargs):
        super(CountryFilter, self).__init__(*args,**kwargs)
        self.filters["user"].label = "User:"

