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

def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial ou para onde você preferir
    else:
        form = TeamForm(instance=team)
    return render(request, 'tasks/edit_team.html', {'form': form, 'team': team})


def delete_team(request, project_id):
    team = get_object_or_404(Team, id=project_id)  # Agora estamos buscando o Time e não o Projeto
    team.delete()  # Exclui o time
    return redirect('home')  # Redireciona para a página inicial (ajuste conforme necessário)

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)  # Certificando-se de pegar o projeto
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('team_projects', team_id=project.team.id)  # Redirecionar para a página do time
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tasks/edit_project.html', {'form': form, 'project': project})


def confirm_delete_project(request, project_id):
    # Obter o projeto para exibir na página de confirmação
    project = get_object_or_404(Project, id=project_id)
    
    # Verifica se o método de solicitação é POST (o usuário clicou para excluir)
    if request.method == 'POST':
        project.delete()  # Exclui o projeto
        return redirect('team_projects', team_id=project.team.id)  # Redireciona para os projetos do time
    
    # Se o método não for POST, apenas renderize a página de confirmação
    return render(request, 'tasks/confirm_delete_project.html', {'project': project})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Se o formulário for enviado (POST)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Salva a tarefa editada
            return redirect('project_tasks', project_id=task.project.id)  # Redireciona para as tarefas do projeto
    else:
        form = TaskForm(instance=task)  # Preenche o formulário com os dados da tarefa

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id  # Guarda o ID do projeto para redirecionar corretamente
    task.delete()  # Exclui a tarefa
    return redirect('project_tasks', project_id=project_id)  # Redireciona para a página de tarefas do projeto
