# pages/urls.py
from django.urls import path

from .views import (HomePageView, AboutPageView, ProjectDetailPage,
                    ProjectCreateView, ProjectEditView, ProjectDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('project/<int:pk>', ProjectDetailPage.as_view(), name='project_detail'),
    path('project/new', ProjectCreateView.as_view(), name='new_project'),
    path('project/edit/<int:pk>', ProjectEditView.as_view(), name='edit_project'),
    path('project/delete/<int:pk>',
         ProjectDeleteView.as_view(), name='delete_project'),
]
