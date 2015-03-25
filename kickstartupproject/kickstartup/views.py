from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to KickStartUp! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("About. <a href="/rango/">Return to Index</a>")
# Create your views here.
