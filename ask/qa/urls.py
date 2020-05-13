from django.contrib import admin
from django.urls import path

urlpatterns = [
	url(r'^$',views.test, name = 'index')
]
