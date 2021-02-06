from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin,)
from atelier_project.settings import LOGIN_URL

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Project


class HomePageView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'all_projects'


class AboutPageView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'about.html'
    context_object_name = 'all_projects'

    login_url = LOGIN_URL


class ProjectDetailPage(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_details.html'

    login_url = LOGIN_URL


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_new.html'
    fields = ['title', 'content']

    login_url = LOGIN_URL

    def form_valid(self, form):
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'edit_project.html'
    fields = ['title', 'content']

    login_url = LOGIN_URL

    def test_func(self):
        print(self)
        return self.get_object().author == self.request.user


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('home')

    login_url = LOGIN_URL

    def test_func(self):
        print(self)
        return self.get_object().author == self.request.user
