from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm

# Create your views here.


def login(request):
    return HttpResponse("Login")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = RegisterForm()
    context = {
        "form":form
    }
    return render(request, "users/register.html",context)