from django.contrib import admin
from django.urls import path
from djapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('analyze', views.analyze, name='analyze'),
    path('about', views.about, name='about')
]
