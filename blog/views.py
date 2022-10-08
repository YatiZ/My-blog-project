from unittest import loader
from django.shortcuts import render
from datetime import date

all_posts = [
    {"slug":"volunteering-journeys",
     "image" : "minions.png",
     "author":"yati",
     "date" : date(2022,5,7),
     "title": "My Volunteering Journeys",
     "excerpt" :"I was one of the member of buddhist organization in university. I incorporated in arranging religious festivals where our inspired monks give speeches for youths what to do and not to do in their lives. ",
     "content":"""
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
     """
    },
    {"slug":"future-plan",
     "image" : "future.jpeg",
     "author":"yati",
     "date" : date(2022,3,7),
     "title": "My Future Plan",
     "excerpt" :"I like calculation and challenging to myself , I became to choose computer science. I have a strong enthusiasm for processing and computer interface related frameworks and innovation. ",
     "content":"""
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
     """
    },
    {"slug":"Education-Background",
     "image" : "minions.png",
     "author":"yati",
     "date" : date(2022,10,7),
     "title": "My Education Background",
     "excerpt" :"I am an electronic engineering student who has been attending at Thanlyin technology university.  As the university had been closed for about 2 years, I have been teaching",
     "content":"""
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
       Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus molestiae temporibus libero modi ipsum rem nobis corrupti aut laudantium tempora quisquam ducimus asperiores animi, natus voluptates optio magni ratione praesentium!
     """
    }
]
# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "index.html",{"posts":latest_posts})

def posts(request):
    return render(request,"all_posts.html",{
        "all_posts":all_posts
    })

def post_detail(request):
    pass

def test(request):
    return render(request,"test.html")

def post_detail(request,slug):
    identified_post=next(post for post in all_posts if post['slug'] == slug)
    return render(request,"post_detail.html",{
        "post":identified_post
    })