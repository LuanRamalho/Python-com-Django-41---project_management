from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    priority_choices = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    priority = models.CharField(max_length=10, choices=priority_choices)
    status_choices = [('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')]
    status = models.CharField(max_length=15, choices=status_choices, default='todo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
