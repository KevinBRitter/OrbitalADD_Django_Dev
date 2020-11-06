from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/site/', views.about_site, name='about_site'),
    path('about/author/', views.about_author, name='about_author'),
]
