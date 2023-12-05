from django.shortcuts import render
from crud.models import Blog


# Create your views here.
def index(request):
    blog=Blog.objects.all()
    blog_new=Blog.objects.all().order_by('create_at') [:1].first()
    blog_picked = Blog.objects.all().exclude(id=blog_new.id).order_by('create_at') [:8]
    blog_old = Blog.objects.all().order_by('-id')
    return render(request,'index.html',{'blog':blog,'blog_picked':blog_picked,'blog_old':blog_old,'blog_new':blog_new})


def aboutus(request):
    return render(request,'aboutus.html',{})


def contactus(request):
    return render(request,'contactus.html',{})

