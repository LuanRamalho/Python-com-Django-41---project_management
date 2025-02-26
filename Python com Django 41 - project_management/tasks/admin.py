# admin.py
from django.contrib import admin
from .models import Team, Project, Task

# Registro dos modelos no Django Admin

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Exibe os campos no painel
    search_fields = ('name', 'description')  # Permite buscar por nome e descrição

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'deadline', 'description')  # Campos visíveis na lista
    list_filter = ('team', 'deadline')  # Filtros para a interface de administração
    search_fields = ('title', 'description')  # Permite buscar por título ou descrição
    ordering = ('deadline',)  # Ordena os projetos pela data de entrega

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'deadline')  # Campos visíveis na lista
    list_filter = ('project', 'status', 'priority')  # Filtros para facilitar a busca
    search_fields = ('title', 'description')  # Permite buscar por título ou descrição
    ordering = ('status', 'priority')  # Ordena as tarefas por status e prioridade
