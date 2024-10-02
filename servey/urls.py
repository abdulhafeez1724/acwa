from django.urls import path
from .views import home_view, profile_view, submit_profile  # Import the submit_profile view

urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('submit-profile/', submit_profile, name='submit_profile'),
    
]
