#from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm



class HomePageView(TemplateView):
    template_name = "auctions/home.html"

    

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



# def index(request):
#     return render(request, "auctions/index.html")


def category(request):
    return render(request, "auctions/category.html")


def watchlist(request):
    return render(request, "auctions/watchlist.html")


def createlisting(request):
    return render(request, "auctions/createlisting.html")