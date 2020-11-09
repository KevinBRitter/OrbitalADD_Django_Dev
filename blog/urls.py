from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/site/', views.about_site, name='about_site'),
    path('about/author/', views.about_author, name='about_author'),
]
