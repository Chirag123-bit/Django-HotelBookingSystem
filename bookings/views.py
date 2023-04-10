from django.shortcuts import render,redirect
from .models import Accomodations,booking


def accomodationDetail(request,id):
    accomodation = Accomodations.objects.get(id=id)
    bookings = booking.objects.filter(accomodation = accomodation)
    valid = True
    if request.user:
        for i in bookings:
            if i.user == request.user:
                print("Found")
                valid=False
            else:
                print("Not Found")

    if(request.method=="POST"):
        data = request.POST
        checkin = data.get("checkin")
        checkout= data.get("checkout")
        accom = Accomodations.objects.get(id=id)
        
        newBooking = booking(user = request.user, accomodation = accom, check_in = checkin, check_out = checkout) 
        newBooking.save()
        return redirect(f"/accomodation/{id}")

    context={
        "acc":accomodation,
        "valid":valid
    }
    return render(request, "bookings/accomodation.html",context)

def getAccomodations(request):
    return render(request, "bookings/search.html")


def myBookings(request):
    bookings={}
    if(request.user):
        bookings = booking.objects.filter(user = request.user)
    context={
        "books":bookings
    }
    
    return render(request,"bookings/mybookings.html",context)