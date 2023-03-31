from django.shortcuts import render


def accomodationDetail(request):
    return render(request, "bookings/accomodation.html")

def getAccomodations(request):
    return render(request, "bookings/search.html")