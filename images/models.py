from django.db import models

# Create your models here.

    
    
class Location(models.Model):
    name = models.CharField(max_length =80)
    def __str__(self):
        return self.name
    
    def save_location():
        pass
    
    def delete_location():
        pass
    

class Category(models.Model):
    name = models.CharField(max_length =80)
    
    def __str__(self):
        return self.name
    
    
    def save_category():
            pass
    
    def delete_category():
        pass
    
    

class Image(models.Model):
    name = models.CharField(max_length =80)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'photos/')
    
    def save_image():
        pass
    
    
    def delete_image():
        pass
    
    
    
    def update_image():
        pass
    
    
    def get_image_by_id(id):
        pass
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        pass
    
    
    
    
    
    