from django.contrib import admin
from django.urls import path, include, re_path
from profiles.router import router

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
