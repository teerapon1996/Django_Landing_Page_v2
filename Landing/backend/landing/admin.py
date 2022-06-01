from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import *
# Register your models here.

class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

admin.site.register(News, NewsAdmin)