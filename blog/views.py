from django.shortcuts import render


# Create your views here.
def index(request):
    page_header = {'page_header': "Home Page"}
    return render(request, 'index.html', page_header)


def about_site(request):
    page_header = {'page_header': "About orbitaladd.com"}
    return render(request, 'about_site.html', page_header)


def about_author(request):
    page_header = {'page_header': "About the Developer"}
    return render(request, 'about_author.html', page_header)
