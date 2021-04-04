from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('news/',views.news, name= 'news'),
    path('gallery/',views.gallery, name = 'gallery'),
    
    path('news/<slug:slug>',views.post, name = 'post'),
    path('team/',views.team, name = 'team'),
    
    path('add-post/',views.addPost, name = 'add_post'),
    
    path('add-member/',views.addExecutive, name = 'add_executive'),
    
    path('login/', views.loginPage, name = 'login_user'),
    path('logout/', views.logoutUser, name = 'logout_user'),
    
    path('update-member/<str:pk>/',views.updateExecutive, name = 'update_executive'),
    path('update-news/<slug:slug>/',views.updatePost, name = 'update_post'),
    path('delete-member/<str:pk>/',views.deleteExecutive, name = 'delete_executive'),
    path('delete-news/<str:slug>/',views.deletePost, name = 'delete_post'),
    
    path('gallery/add-image/',views.addImage, name = 'add_image'),
    path('gallery/delete-image/<str:pk>/',views.deleteImage, name = 'delete_image'),
    path('gallery/delete-event/<str:pk>/',views.deleteEvent, name = 'delete_event'),
    
    path('donate/',views.donate, name = 'donate'),
    
]