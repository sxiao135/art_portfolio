"""
URL configuration for PORTFOLIO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name="testing"),
    path('about', views.about, name="about"),
    path('homepage', views.homepage, name="homepage"),
    path('studies', views.studies, name="studies"),
    path('digital', views.digital, name="digital"),
    # path('homepage', views.portfolio_page, {'tag': 'fp'}, name="homepage"), #for the portfolio_pge function
    # path('studies', views.portfolio_page, {'tag': 'study'}, name="studies"),
    # path('digital', views.portfolio_page, {'tag': 'digital'}, name="digital"),
    # path('studies/<int:image_id>/', views.image_detail, name='image_detail'), #these are repetitive, not sure how to fix yet
    # path('digital/<int:image_id>/', views.image_detail, name='image_detail'),
    # path('homepage/<int:image_id>/', views.image_detail, name='image_detail'),
]
