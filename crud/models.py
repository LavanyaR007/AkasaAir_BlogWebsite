from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50)
    icon=models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many to one relation with Category
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title=models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    content=RichTextField()
    image = models.ImageField(upload_to='images/', null=False)
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='images/')


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=250,blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']