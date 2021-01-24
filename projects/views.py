from django.views.generic import ListView, DetailView
from .models import Project


class HomePageView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'all_projects'


class AboutPageView(ListView):
    model = Project
    template_name = 'about.html'
    context_object_name = 'all_projects'


class ProjectDetailPage(DetailView):
    model = Project
    template_name = 'project_details.html'
