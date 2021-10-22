from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth.views import login_required,logout_then_login


