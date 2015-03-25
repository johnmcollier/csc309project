from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'kickstartup/index.html', context_dict)

def about(request):
    return HttpResponse("About. <a href='/kickstartup/'>Return to Index</a>")
# Create your views here.
