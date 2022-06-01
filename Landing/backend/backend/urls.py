from unicodedata import name
from django.contrib import admin
from django.urls import path, include # New
from django.views.generic import TemplateView # New
from landing import views
from django.conf import settings # Import settings.py
from django.conf.urls.static import static  #Upload imgs static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #Upload imgs static
from django.conf.urls.i18n import i18n_patterns # Translate en/th
from django.utils.translation import gettext_lazy as _ # Translate en/th

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('api/', include('api.urls')),
    path('',include('landing.urls')),
    
]

urlpatterns += i18n_patterns (
    path('', include('landing.urls')) # Translate /en/,/th/
)

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #Upload imgs staic 
