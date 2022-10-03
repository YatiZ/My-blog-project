from unittest import loader
from django.shortcuts import render


# Create your views here.
def starting_page(request):
    return render(request, "index.html")

def posts(request):
    return render(request,"all_posts.html")

def post_detail(request):
    pass

def test(request):
    return render(request,"test.html")