from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from kickstartup.models import UserProfile, Industry, StartUp, Keywords
from kickstartup.forms import UserForm, UserProfileForm

# Index view
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'kickstartup/index.html', context_dict)

# View for the about page. Not gonna bother doing anything with it since it's not part of the marking scheme
def about(request):
    return HttpResponse("About. <a href='/kickstartup/'>Return to Index</a>")

# Register page view
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
    
    context_dict = {'registered': registered, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'kickstartup/register.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Use django's authentication system to verify that the credentials are correct
        user = authenticate(username=username, password=password)
        
        # Check that the user exists
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/kickstartup/startups/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    
    else:
        return render(request, 'kickstartup/login.html', {})
    
# View for logging out
# Django does the deletion of the session / cookie management    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/kickstartup/')

def startups(request):
    startups = StartUp.objects.all()
    context_dict = {'startups': startups}
    return render(request, 'kickstartup/startups.html', context_dict)

def startup(request, startup_name_slug):
    context_dict = {}
    
    try:
        startup = StartUp.objects.get(slug=startup_name_slug)
        context_dict['startup'] = startup
        context_dict['startup_name_slug'] = startup_name_slug
    except StartUp.DoesNotExist:
        pass
    return render(request, 'kickstartup/startup.html', context_dict)
# Create your views here.
