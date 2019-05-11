from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc1= Location(name = 'Nairobi')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(name = 'Sport')




class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.image1= Location(name = 'Nairobi')
        self.image1.save_location()
        
        self.new_image= Image(name = 'Amboseli',description = 'This is a random post',location = self.image1)
        self.new_image.save()




