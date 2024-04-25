from django.urls import path
from .views import homePageView, about, modelsPageView

urlpatterns = [
    path('', homePageView, name='Home'),
    path("about", about, name="about"),
    path('models', modelsPageView, name='models')
]