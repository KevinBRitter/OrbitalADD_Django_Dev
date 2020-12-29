from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def dashboard(request):
    page_header = {'page_header': "Home Page"}
    return render(request, 'dashboard.html', page_header)


def about_site(request):
    page_header = {'page_header': "About orbitaladd.com"}
    return render(request, 'about_site.html', page_header)


def about_author(request):
    page_header = {'page_header': "About the Developer"}
    return render(request, 'about_author.html', page_header)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
