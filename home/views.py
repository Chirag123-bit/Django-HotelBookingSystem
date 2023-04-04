from django.shortcuts import render
from django.http import HttpResponse
from bookings.models import Accomodations


# Create your views here.


def homePage(request):
    featured = Accomodations.objects.all()[:3]
    context = {
        "featured":featured
    }
    print(featured)
    return render(request,"home/homepage.html",context)




