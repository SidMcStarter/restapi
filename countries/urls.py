from django.urls import path
from . import views

urlpatterns = [
    path("",views.CountriesViews.as_view(),name="home"),
    path("country/<str:country>/<int:pk>/",views.CountryDetailView.as_view(), name="country"),
    path("country/create/",views.CreateCountryView.as_view(),name="create_country"),
    path("country/update/<str:country>/<int:pk>",views.UpdateCountryView.as_view(),name="update_country"),
    path("country/delete/<int:pk>", views.DeleteCountryView.as_view(),name="delete_country"),
    path("delete/all",views.delete_all,name="delete_all"),
    path("populate",views.populate,name="populate")
]