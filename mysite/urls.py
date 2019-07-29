"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView # new

from news.views import index
from news.views import about

from django.views.static import serve
from mysite.settings import MEDIA_ROOT
from django.conf.urls import url



urlpatterns = [
    path('news/', include('news.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new

    path('accounts/', include('django.contrib.auth.urls')), # new
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', index, name='home'),
    path('about.html', about, name='about'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^(?P<page>\d+)/$', index, name='home'),
]
