from django.urls import path

from . import views

urlpatterns = [
    path('myprofile', views.userprofile, name='myprofile'),
    path('userupdate',views.user_update,name='userupdate')
]