from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView

def index(request):    
    return render(request, 'index.html')

def nmap(request) :
    return render(request, 'nmap.py')

def speedtest(request) :
    return render(request, 'speedtest.py')

def main(request) :
    return render(request, 'main.py')

def pingcheck(request) :
    return render(request, 'pingcheck.py')

def webstatus(request) :
    return render(request, 'webstatus.py')

def dependencies(request) :
    return render(request, 'dependencies.py')

def interfaces(request) :
    return render(request, 'interfaces.py')