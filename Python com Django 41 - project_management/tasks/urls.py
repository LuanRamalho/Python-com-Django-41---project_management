from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/<int:team_id>/projects/', views.team_projects, name='team_projects'),
    path('project/<int:project_id>/tasks/', views.project_tasks, name='project_tasks'),
    path('project/<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('team/<int:team_id>/add_project/', views.add_project, name='add_project'),
    path('add_team/', views.add_team, name='add_team'),
]
