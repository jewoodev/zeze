from django.urls import path

from . import views
from .views import FlightListAPI

urlpatterns = [
    path('', views.search_flights, name="search_flights"),
    path('result_flight_list/', views.result_flight_list, name="result_flight_list"),
    path('api/flight/', FlightListAPI.as_view()),
]