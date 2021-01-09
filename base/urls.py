from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('news/',views.news, name= 'news'),
    path('gallery/',views.gallery, name = 'gallery'),
    path('contact/',views.contact, name = 'contact'),
    path('news/<slug:slug>',views.post, name = 'post'),
    path('team/',views.team, name = 'team'),
    
    path('add-post/',views.addPost, name = 'add_post'),
    path('add-member/',views.addMember, name = 'add_member'),
    
    path('login/', views.loginPage, name = 'login_user'),
    path('logout/', views.logoutUser, name = 'logout_user'),
    
]