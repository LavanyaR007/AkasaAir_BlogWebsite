from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class UserProfile(models.Model):
    gen = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=250, null=True)
    image = models.ImageField(blank=True, upload_to='images/users/')
    cover_image = models.ImageField(upload_to='images/users/', null=True, default='images/cover.jpg')
    gender = models.CharField(choices=gen, max_length=6, null=True)
    facebooklink = models.CharField(blank=True,null=True, max_length=20000)
    twitterlink = models.CharField(blank=True,null=True, max_length=20000)
    instagramlink = models.CharField(blank=True, null=True, max_length=20000)
    youtubelink = models.CharField(blank=True, null=True, max_length=20000)
    emaillink = models.CharField(blank=True, null=True, max_length=20000)
    phone=models.IntegerField(blank=True,null=True,max_length=10)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'