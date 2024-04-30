from django.urls import path
from .views import homePageView, about

urlpatterns = [
    path('', homePageView, name='Home'),
    path("about", about, name="about")
]