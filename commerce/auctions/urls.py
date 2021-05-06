from django.urls import path

from . import views
from .views import HomePageView, RegisterView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("category", views.category, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("createlisting", views.createlisting, name="createlisting"),
]
