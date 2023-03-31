
from django.urls import path
from . import views

urlpatterns = [
    path("", views.accomodationDetail),
    path("rooms/", views.getAccomodations),
    
]
