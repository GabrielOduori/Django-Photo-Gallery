from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def index(request):
    '''
    Index function loads the start up page with a filter of randon six images at the beginning
    '''
    gallery = Image.objects.all()[:6]
    return render(request,'index.html', {'gallery':gallery})


def gallery(request):
    '''
    gallery function returns the list of photos in the database
    '''
    gallery = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery':gallery})

def single_image_details(request,image_id):
    '''
    Function that returns details of a single image. This will be in a modal views
    '''
    image_detail = get_object_or_404(Image, pk=image_id)
    return render(request,'gallery/details.html', {'image_detail':image_detail})


def about_us(request):
    '''
    Function that returns information abous us
    '''
    return render(request, 'about/about.html')



def blog(request):
    '''
    This is a function we can use in future to add a blog onto the application
    '''
    pass



def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term  =  request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message  = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})
    else:
        message = "You have not searched for any category"
        
        return render(request, 'search.html', {"message":message})


def sports(request):
    sports_category = Category.objects.get(pk=1)
    sports = Image.objects.all().filter(category=sports_category)
    return render(request,'category/sports/sports.html', {'sports':sports})


def nature(request):
    nature_category = Category.objects.get(pk=2)
    nature = Image.objects.filter(category=nature_category)
    return render(request,'category/nature/nature.html', {'nature':nature})


def entertainment(request):
    ente_category = Category.objects.get(pk=5)
    entertainment = Image.objects.filter(category=ente_category)
    return render(request,'category/entertainment/entertainment.html', {'entertainment':entertainment})

def technology(request):
    tech_category = Category.objects.get(pk=3)
    tech = Image.objects.filter(category=tech_category)
    return render(request,'category/technology/technology.html', {'tech':tech})


# def image(request,image_id):
#     try:
#         image = Image.objects.get(id=image_id)
#     except: DoesNotExist
#         raise Http404
#     return render(request, 'image.html',{"image":image})