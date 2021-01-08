from django.db import models
from datetime import date,time,datetime
from django.utils.text import slugify

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null = True, blank = True, upload_to = 'images', default = 'user-image.jpg')
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length = 14)
    position = models.OneToOneField(Position, on_delete = models.SET_NULL, null=True)
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    about = models.TextField(null = True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    description = models.CharField(max_length=250)
    image = models.ImageField()
    date = models.DateField()
    
    def __str__(self):
        return self.description
    
class Post(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/posts', null = True, blank = True )
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank = True, null=True)
    
    
    def __str__(self):
        return self.heading
    
    def save(self,*args,**kwargs):
        
        if self.slug == None:
            slug = slugify(self.heading)
            
            has_slug = Post.objects.filter(slug = slug).exists()
            count = 0
            while has_slug:
                count +=1 
                slug = slugify(self.heading)+ '-' + str(count)
                has_slug = Post.objects.filter(slug = slug).exists()
                
            self.slug = slug
        super().save(*args,**kwargs)