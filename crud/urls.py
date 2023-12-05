from django.urls import path

from . import views

urlpatterns = [
    path('category/<int:id>/', views.category, name='category'),
    path('blogdetail/<int:id>/<slug:slug>/',views.blogdetail, name='blogdetail'),
    path('addblog',views.addblog,name='addblog'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('updateblog/<int:id>/<slug:slug>/',views.editblog,name='updateblog'),
    path('deleteimage/<int:id>/',views.deleteimage,name='deleteimage'),
    path('deleteblog/<int:id>/<slug:slug>/',views.deleteblog,name='deleteblog'),
    path('addcomment/<int:id>/',views.addcomment,name='addcomment')
]