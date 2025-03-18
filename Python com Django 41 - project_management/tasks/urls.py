from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/<int:team_id>/projects/', views.team_projects, name='team_projects'),
    path('project/<int:project_id>/tasks/', views.project_tasks, name='project_tasks'),
    path('project/<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('team/<int:team_id>/add_project/', views.add_project, name='add_project'),
    path('add_team/', views.add_team, name='add_team'),
    path('team/<int:team_id>/edit/', views.edit_team, name='edit_team'),
    path('project/<int:project_id>/delete/', views.delete_team, name='delete_team'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),  
    path('project/<int:project_id>/confirm_delete/', views.confirm_delete_project, name='confirm_delete_project'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),

]
