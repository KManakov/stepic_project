"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = patterns('qa.views',
        url(r'^$', 'index', name='index'),
        url(r'^login/', 'login', name='login'),
        url(r'^signup/', 'signup', name='signup'),
        url(r'^question/(?P<quest_id>[0-9]+)/$', 'question', name'question'),
        url(r'^ask/', 'ask', name='ask'),
        url(r'^answer/', 'answer', name='answer'),
        url(r'^popular/', 'popular', name='popular'),
        url(r'^new', 'test', name='new')
)