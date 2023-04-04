from django.shortcuts import render,redirect
from .models import Accomodations,booking


def accomodationDetail(request,id):
    accomodation = Accomodations.objects.get(id=id)
    if(request.method=="POST"):
        data = request.POST
        checkin = data.get("checkin")
        checkout= data.get("checkout")
        accom = Accomodations.objects.get(id=id)
        
        newBooking = booking(user = request.user, accomodation = accom, check_in = checkin, check_out = checkout) 
        newBooking.save()
        return redirect(f"/accomodation/{id}")

    context={
        "acc":accomodation
    }
    print(context)
    return render(request, "bookings/accomodation.html",context)

def getAccomodations(request):
    return render(request, "bookings/search.html")