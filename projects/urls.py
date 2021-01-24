# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView, ProjectDetailPage


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('project/<int:pk>', ProjectDetailPage.as_view(), name='project_detail')
]
