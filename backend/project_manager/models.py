from django.db import models
from accounts.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=750, null=True, blank=True)
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    
    def __str__(self):
        return f'{self.name} - created by {self.creator}'
    

class Member(models.Model):
    name = models.CharField(max_length=50)
    
    account = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')    
    
    def __str__(self):
        return self.name
    
    
class Role(models.Model):
    # enumaration types: https://docs.djangoproject.com/en/5.2/ref/models/fields/#enumeration-types
    class RoleType(models.TextChoices):
        MANAGER = 'manager'
        WORKER = 'worker'
    
    role = models.CharField(max_length=50, choices=RoleType.choices)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='roles')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='roles')
    
    def __str__(self):
        return f'{self.member} is a {self.role} at {self.project}'
    

class ProjectCharter(models.Model):
    document = models.FileField(upload_to='documents/project_charters/')
    last_updated = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project charters')
    
    def __str__(self):
        return f'{self.project}\'s project charter'
    

class WorkBreakdownStructure(models.Model):
    document = models.FileField(upload_to='documents/work_breakdown_structures/')
    last_updated = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='work breakdown structures')
    
    def __str__(self):
        return f'{self.project}\'s work breakdown structure'


class Report(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')
    
    def __str__(self):
        return f'{self.title} ({self.project}) - {self.created_at}'
    

class KanbanBoard(models.Model):
    card_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='kanban boards')
    
    def __str__(self):
        return f'{self.project}\'s kanban board'
    

class KanbanCard(models.Model):
    class StatusType(models.TextChoices):
        TODO = 'to do'
        IN_PROGRESS = 'in progress'
        TESTING = 'testing'
        DONE = 'done'
        
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=StatusType.choices)
    
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE, related_name='cards')
    responsible_members = models.ManyToManyField(Member, blank=True, related_name='tasks')
    
    def __str__(self):
        return f'{self.task} - {self.status}'