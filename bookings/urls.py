
from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.accomodationDetail, name="acc_detail"),
    path("rooms/", views.getAccomodations),
    
]
