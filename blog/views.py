from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about_site(request):
    return render(request, 'about_site.html')


def about_author(request):
    return render(request, 'about_author.html')
