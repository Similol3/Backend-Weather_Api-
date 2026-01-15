from django.urls import path
from weather1.views import WeatherDetailView

urlpatterns = [
    path('weather/', WeatherDetailView.as_view(), name='weather-detail')
]
