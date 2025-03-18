from django import forms
from .models import Project, Task, Team

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'deadline', 'team']
        widgets = {
            'deadline': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'status', 'project']
        widgets = {
            'deadline': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description']
