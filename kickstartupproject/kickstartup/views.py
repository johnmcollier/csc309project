from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to KickStartUp! <br /> <br /> <a href='/kickstartup/about/'>About</a>")

def about(request):
    return HttpResponse("About. <a href='/kickstartup/'>Return to Index</a>")
# Create your views here.
