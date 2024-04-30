from django.urls import path
from .views import PostPageView

urlpatterns = [
    path('', PostPageView.as_view(), name='home') # this work with classes
]

# urlpatterns = [
#     path('', PostPageView, name='home') # this work with render
# ]