from django.urls import path
from .views import home, random_website  # Import both views

urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('random/', random_website, name='random_website'),  # Random Website Redirect
]
