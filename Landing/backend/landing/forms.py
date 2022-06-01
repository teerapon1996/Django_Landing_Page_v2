from django import forms
from .models import *
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    image = forms.ImageField()
    descriptions = RichTextField()

    class Meta:
        model  = News
        fields = ('title','image','descriptions',)
