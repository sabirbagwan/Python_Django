from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
from .models import Contact
from django.utils.html import format_html

def index(request):

    featured = Post.objects.filter(featured=True)
    posts = Post.objects.all().reverse()[:3]
    latests = Post.objects.all().order_by('-add_date')[:3]
    data = {
        'posts': posts,
        'featured': featured,
        'latests' : latests,
    }
    return render(request, 'index.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    allposts = Post.objects.all()[:11]
    sidebarallposts = Post.objects.all().order_by('-add_date')
    data = {
        'allposts': allposts,
        'post':post,
        'sidebarallposts' : sidebarallposts,
    }
    return render(request, 'post.html', data)

def allblogs(request):
    allposts = Post.objects.all().order_by('-add_date')
    data = {
        'allposts' : allposts,
    }
    return render(request,'allblogs.html', data)


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(name) < 3 or len(email) < 5 or len(message) < 5:
            messages.error(request, 'Please fill all the fields. Thank you!')

        else:
            contact = Contact(name=name, email=email,message=message, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent. Thank you!')
    return render(request, 'contact.html')

