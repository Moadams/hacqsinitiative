from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('news/',views.news, name= 'news'),
    path('gallery/',views.gallery, name = 'gallery'),
    path('contact/',views.contact, name = 'contact'),
    path('news/<slug:slug>',views.post, name = 'post'),
]