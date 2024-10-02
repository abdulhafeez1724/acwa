from django.shortcuts import render
from .models import NewProfile  # Import the new model
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import NewProfile  # Import the new model

def home_view(request):
    return render(request, 'servey/index.html')

def profile_view(request):
    return render(request, 'servey/profile.html')


    

def submit_profile(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')  # Get first name
        lname = request.POST.get('lname')  # Get last name
        office = request.POST.get('office')  # Get office location
        quote = request.POST.get('quote')  # Get quote

        # Create a new NewProfile instance and save it
        new_profile = NewProfile(fname=fname, lname=lname, office=office, quote=quote)
        new_profile.save()

        # Optionally, redirect to a success page or back to the profile page
        return redirect('home')  # Change 'home' to the desired URL name

    return render(request, 'servey/profile.html')  # Render the form again if not a POST request
