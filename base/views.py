from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import AddPostForm,AddExecutiveForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.



# -------------------------------------------------------------------------------------
#                                     LOGIN VIEW
# -------------------------------------------------------------------------------------
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


# -------------------------------------------------------------------------------------
#                                   LOGOUT VIEW
# -------------------------------------------------------------------------------------

def logoutUser(request):
    logout(request)
    return redirect('home')



# -------------------------------------------------------------------------------------
#                                   HOME VIEW
# -------------------------------------------------------------------------------------

def home(request):
    executives = Executive.objects.all()[0:3]
    
    context = {
        'executives':executives
    }
    return render(request, 'index.htm',context)


# -------------------------------------------------------------------------------------
#                                   ABOUT VIEW
# -------------------------------------------------------------------------------------

def about(request):
    return render(request, 'about.htm')




# -------------------------------------------------------------------------------------
#                                   NEWS VIEW
# -------------------------------------------------------------------------------------
def news(request):
    news = Post.objects.all()
    context = {
        'news':news
    }
    return render(request,'news.htm',context)




# -------------------------------------------------------------------------------------
#                         GALLERY VIEW
# -------------------------------------------------------------------------------------
def gallery(request):
    event = request.GET.get('event')
    
    
    
    if event == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(event__event_name = event)
    
    events = Event.objects.all()
    
    page = request.GET.get('page')
    paginator = Paginator(images,20)
    
    try: 
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    
    context = {
        'events':events,
        'images':images
    }
    return render(request, 'gallery.htm',context)


# -------------------------------------------------------------------------------------
#                        ADD IMAGE VIEW
# -------------------------------------------------------------------------------------
def addImage(request):
    events = Event.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        # image = request.FILES.get('image')
        
        if data['event'] != 'none':
            event = Event.objects.get(id = data['event'])
        elif data['new_event'] != '':
            event, created = Event.objects.get_or_create(event_name = data['new_event'])
        else:
            event = None
        
        for image in images:
            image = Image.objects.create(
                event = event,
                image = image
            )
        
        return redirect('gallery')
    
    context = {
        'events':events
    }
    return render(request,'forms/add-image.htm',context)


# -------------------------------------------------------------------------------------
#                                   DELETE IMAGE
# -------------------------------------------------------------------------------------
def deleteImage(request,pk):
    Image.objects.get(id = pk).delete()
    return redirect('gallery')

# -------------------------------------------------------------------------------------
#                                   DELETE EVENT
# -------------------------------------------------------------------------------------
def deleteEvent(request,pk):
    Event.objects.get(id = pk).delete()
    return redirect('gallery')


# -------------------------------------------------------------------------------------
#                          POST VIEW
# -------------------------------------------------------------------------------------
def post(request,slug):
    post = Post.objects.get(slug = slug)
    context = {
        'post':post
    }
    return render(request,'post.htm',context)



# -------------------------------------------------------------------------------------
#                               TEAM VIEW
# -------------------------------------------------------------------------------------

def team(request):
    executives = Executive.objects.all()
    context = {
        'executives':executives
    }
    return render(request,'team.htm',context)



# -------------------------------------------------------------------------------------
#                         ADD POST VIEW
# -------------------------------------------------------------------------------------

def addPost(request):
    postForm = AddPostForm()
    
    if request.method == 'POST':
        postForm = AddPostForm(request.POST,request.FILES)
        if postForm.is_valid():
            postForm.save()
            return redirect('home')
    
    context = {
        'form':postForm
    }
    
    return render(request,'forms/add-post.htm',context)



# -------------------------------------------------------------------------------------
#                        ADD EXECUTIVE VIEW
# -------------------------------------------------------------------------------------

def addExecutive(request):
    executiveForm = AddExecutiveForm()
    
    if request.method == 'POST':
        executiveForm = AddExecutiveForm(request.POST,request.FILES)
        if executiveForm.is_valid():
            executiveForm.save()
            return redirect('team')
        
    context= {
        'form':executiveForm
    }
    return render(request, 'forms/add-member.htm',context)


# -------------------------------------------------------------------------------------
#                        UPDATE EXECUTIVE VIEW
# -------------------------------------------------------------------------------------

def updateExecutive(request,pk):
    executive = Executive.objects.get(id=pk)
    executiveForm = AddExecutiveForm(instance=executive)
    
    if request.method == 'POST':
        executiveForm = AddExecutiveForm(request.POST,instance = executive)
        if executiveForm.is_valid():
            executiveForm.save()
            return redirect('team')
    
    context = {
        'executive':executive,
        'form':executiveForm
    }
    
    return render(request,'forms/update-member.htm',context)



# -------------------------------------------------------------------------------------
#                        DELETE EXECUTIVE VIEW
# -------------------------------------------------------------------------------------

def deleteExecutive(request,pk):
    Executive.objects.get(id=pk).delete()
    # member.delete()
    return redirect('team')


# -------------------------------------------------------------------------------------
#                        UPDATE POST VIEW
# -------------------------------------------------------------------------------------

def updatePost(request,slug):
    post = Post.objects.get(slug = slug)
    postForm = AddPostForm(instance=post)
    
    if request.method == 'POST':
        postForm = AddPostForm(request.POST,instance = post)
        if postForm.is_valid():
            postForm.save()
            return redirect('news')
    
    context = {
        'form':postForm
    }
    return render(request,'forms/update-member.htm',context)



# -------------------------------------------------------------------------------------
#                        DELETE POST VIEW
# -------------------------------------------------------------------------------------

def deletePost(request,slug):
    Post.objects.get(slug = slug).delete()
    
    return redirect('news')



# -------------------------------------------------------------------------------------
#                        DONATE VIEW
# -------------------------------------------------------------------------------------
def donate(request):
    return render(request, 'donate.htm')