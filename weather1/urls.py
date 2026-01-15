from django.urls import path
from weather1.views import WeatherDetailView

urlpatterns = [
        path('api/', include('weather1.urls')),]
