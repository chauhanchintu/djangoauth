
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')





@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("dashboard", dashboard, name="dashboard"),
    path('accounts/', include('allauth.urls')),
]
