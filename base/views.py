from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import AddPostForm,AddMemberForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Incorrect Username or Password(They are case sensitive)")
    return render(request,'login.htm')


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    members = Member.objects.all()[0:3]
    
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

def team(request):
    executives = Member.objects.all()
    context = {
        'executives':executives
    }
    return render(request,'team.htm',context)


def addPost(request):
    postForm = AddPostForm()
    
    if request.method == 'POST':
        postForm = AddPostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect('home')
    
    context = {
        'form':postForm
    }
    
    return render(request,'forms/add-post.htm',context)


def addMember(request):
    memberForm = AddMemberForm()
    
    if request.method == 'POST':
        memberForm = AddMemberForm(request.POST)
        if memberForm.is_valid():
            memberForm.save()
            return redirect('home')
        
    context= {
        'form':memberForm
    }
    return render(request, 'forms/add-member.htm',context)