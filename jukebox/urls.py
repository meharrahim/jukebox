"""jukebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from jukebox_core.slack_events.views import Events                                    #

urlpatterns = [
    path('', include('jukebox_core.pages.urls')),
    # path('admin/', admin.site.urls),
    url(settings.ADMIN_URL,admin.site.urls),
    path('users/', include('jukebox_core.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    url(r'^votingapp/', include('jukebox_core.votingapp.urls')),
    url(r'^events/', Events.as_view()),                            #

]
