from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.
def index(request):
    return render(request,'index.html')



def gallery(requst):
    
    gallery = Image.objects
    return render(requst, 'gallery/gallery.html', {'gallery':gallery})



def about_us(request):
    return render(request, 'about/about.html')



def blog(request):
    pass


def single_image_view(request,id):
    pass


