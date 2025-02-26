from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, Team
from .forms import ProjectForm, TaskForm, TeamForm

def home(request):
    teams = Team.objects.all()
    return render(request, 'tasks/home.html', {'teams': teams})

def team_projects(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    projects = Project.objects.filter(team=team)
    return render(request, 'tasks/team_projects.html', {'team': team, 'projects': projects})

def project_tasks(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/project_tasks.html', {'project': project, 'tasks': tasks})

def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_tasks', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

def add_project(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.team = team
            project.save()
            return redirect('team_projects', team_id=team.id)
    else:
        form = ProjectForm()
    return render(request, 'tasks/add_project.html', {'form': form, 'team': team})

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial após adicionar o time
    else:
        form = TeamForm()
    return render(request, 'tasks/add_team.html', {'form': form})
