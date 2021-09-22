from django.shortcuts import render
from django.http import HttpResponse
from . import control
# Create your views here.
# Return data to the user here


def index(request):
    control.controller()
    return render(request, 'FetchAndStoreData/index.html')
