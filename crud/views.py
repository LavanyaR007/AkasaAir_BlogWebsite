from django.shortcuts import render
from .forms import BlogForm, CategoryForm, SearchForm
from .models import Images,Blog,Category,Comment,CommentForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
def category(request,id):
    if id==0:
        category=Category.objects.all()
        blog = Blog.objects.all()
        catdata=0
    else:
        category = Category.objects.all()
        catdata = Category.objects.get(pk=id)
        blog = Blog.objects.filter(category_id=id).order_by('-create_at')

    return render(request, 'cat_blog.html', {'category': category,'blog': blog, 'catdata': catdata})

@login_required(login_url='/login') # Check login
@csrf_exempt
def addcategory(request):
    catform=CategoryForm
    if request.method=='POST':
        catform=CategoryForm(request.POST,request.FILES)
        if catform.is_valid():
            catform.save()
            messages.success(request, 'Category is added Successfully')
            return HttpResponseRedirect('/user/myprofile')
        else:
            messages.warning(request, catform.errors)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return render(request,'addcategory.html',{'catform':catform})

@login_required(login_url='/login') # Check login
@csrf_exempt
def addblog(request):
    blogform=BlogForm()
    if request.method=='POST':
        blogform=BlogForm(request.POST,request.FILES)
        if blogform.is_valid():
            blog=blogform.save(commit=False)
            blog.user = request.user
            blog.slug=slugify(blog.title)
            blog.save()

            image=request.FILES.getlist('image')
            for img in image:
                Images.objects.create(blog=blog, image=img)

            messages.success(request, 'Your blog is posted successfully')
            return HttpResponseRedirect('/user/myprofile')
        else:
            messages.warning(request, blogform.errors)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return render(request,'add_blog.html',{'blogform':blogform})


@login_required(login_url='/login') # Check login
@csrf_exempt
def blogdetail(request,id,slug):
    category=Category.objects.all()
    blog=Blog.objects.get(pk=id)
    blog.views=blog.views+1
    blog.save()
    related_posts = Blog.objects.filter(category=blog.category).exclude(id=id).order_by('?')[:2]
    com=Comment.objects.filter(blog_id=id)
    images = Images.objects.filter(blog_id=id)
    return render(request,'blog_detail.html',{'category':category,'blog':blog,'related_posts':related_posts,'images':images,'com':com})


@login_required(login_url='/login') # Check login
@csrf_exempt
def editblog(request,id,slug):
    blog=Blog.objects.get(pk=id)
    images = Images.objects.filter(blog_id=id)
    update=BlogForm(instance=blog)
    if request.method=='POST':
        update = BlogForm(request.POST, request.FILES, instance=blog)
        if update.is_valid():
            print("saving")
            update.save()

        image = request.FILES.getlist('image')
        for img in image:
            Images.objects.create(blog=blog, image=img)

            messages.success(request,'Your Blog Has been updated successfully')
            return HttpResponseRedirect('/user/myprofile')
        else:
            messages.warning(request, update.errors)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return render(request,'updateblog.html',{'blog':blog,'images':images,'update':update})


@login_required(login_url='/login') # Check login
def deleteimage(request,id):
    Images.objects.filter(id=id).delete()
    messages.success(request, 'Image is Deleted')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required(login_url='/login') # Check login
def deleteblog(request,id,slug):
    Blog.objects.filter(id=id).delete()
    messages.success(request, 'Your Blog is Deleted')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def search(request):
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            query=form.cleaned_data['query']
            blog=Blog.objects.filter(title__icontains=query)
            category=Category.objects.all()

            return render(request,'searchblog.html',{'blog':blog,'query':query,'category':category})

    return HttpResponseRedirect('/')


@login_required(login_url='/login') # Check login
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data=Comment()
            data.comment=form.cleaned_data['comment']
            data.blog_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.status=True
            blog=Blog.objects.get(id=data.blog_id)
            data.save()

            messages.success(request, "Your review has been recorded.Thank You!!")
            return HttpResponseRedirect(url)

        return HttpResponseRedirect(url)