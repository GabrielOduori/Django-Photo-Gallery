from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.
def index(request):
    return render(request,'index.html')
