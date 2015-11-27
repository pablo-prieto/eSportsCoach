"""esport_tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from sideapp import views

urlpatterns = [
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$',RedirectView.as_view(url='/sideapp/'), name='home'),
    url(r'^signup/', 'sideapp.views.login'), #login
   # url(r'^home/$', 'sideapp.views.home'),
    url(r'^logout/$', 'sideapp.views.logout'), #logout
    url(r'^sideapp/', include('sideapp.urls', namespace="sideapp")),
    url(r'^admin/', include(admin.site.urls)),
]
