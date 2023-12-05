from ckeditor.fields import RichTextField
from django import forms
from django.forms import TextInput, EmailInput, Select, FileInput, NumberInput
from crud.models import Blog,Category


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields = ['category', 'title', 'description','content' ,'image','status']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'Category'}),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'Blog Title'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'Blog Description'}),
            'content': RichTextField(),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
            'status': Select(attrs={'class': 'input', 'placeholder': 'Status'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['title','icon','status']
        widgets={
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'Category Title'}),
            'icon' : FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
            'status': Select(attrs={'class': 'input', 'placeholder': 'Status'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)