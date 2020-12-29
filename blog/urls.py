from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/site/', views.about_site, name='about_site'),
    path('about/author/', views.about_author, name='about_author'),

    url(r"^accounts/", include("django.contrib.auth.urls")),

    path('blog/', views.post_list, name='post_list'),
]
