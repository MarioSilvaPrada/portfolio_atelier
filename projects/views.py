from django.views.generic import ListView
from .models import Project


class HomePageView(ListView):
    model = Project
    template_name = 'home.html'


class AboutPageView(ListView):
    model = Project
    template_name = 'about.html'
