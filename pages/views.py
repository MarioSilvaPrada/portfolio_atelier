from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from projects.models import Project


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


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_new.html'
    fields = ['title', 'content', 'author']


class ProjectEditView(UpdateView):
    model = Project
    template_name = 'edit_project.html'
    fields = ['title', 'content']

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('home')