from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    members = Member.objects.all()
    
    context = {
        'members':members
    }
    return render(request, 'index.htm',context)

def about(request):
    return render(request, 'about.htm ')

def news(request):
    news = Post.objects.all()
    context = {
        'news':news
    }
    return render(request,'news.htm',context)

def gallery(request):
    return render(request, 'gallery.htm')

def contact(request):
    return render(request,'contact.htm')

def post(request,slug):
    post = Post.objects.get(slug = slug)
    context = {
        'post':post
    }
    return render(request,'post.htm',context)