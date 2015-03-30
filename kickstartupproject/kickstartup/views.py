from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from kickstartup.models import UserProfile, Industry, StartUp, Keywords
from kickstartup.forms import UserForm, UserProfileForm

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'kickstartup/index.html', context_dict)

def about(request):
    return HttpResponse("About. <a href='/kickstartup/'>Return to Index</a>")

def register(request):
    registered = False
    if request.method == 'POST':
        # grab the user form information from the page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user form data to the DB
            user = user_form.save()
            
            # Hash the user's password
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context_dict = {'registered': registered}
    return render(request, 'kickstartup/register.html', context_dict)
# Create your views here.
