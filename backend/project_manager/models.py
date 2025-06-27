from django.db import models
from accounts.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    current_status = models.TextField(max_length=5000, null=True, blank=True)
    
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
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_charters')
    
    def __str__(self):
        return f'{self.project}\'s project charter'
    

class WorkBreakdownStructure(models.Model):
    document = models.FileField(upload_to='documents/work_breakdown_structures/')
    last_updated = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='work_breakdown_structures')
    
    def __str__(self):
        return f'{self.project}\'s work breakdown structure'


class StatusReport(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/status_reports/')
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='status_reports')
    
    def __str__(self):
        return f'{self.title} ({self.project}) - {self.created_at}'
    

class KanbanBoard(models.Model):
    card_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='kanban_boards')
    
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
    
    def save(self, *args, **kwargs):
        # indicates if a new card is being created 
        is_new = self.pk is None
        
        super().save(*args, **kwargs)
        
        # if a new card was created, updates the card_count of that card's board
        if is_new:
            self.board.card_count += 1
            self.board.save()

    def delete(self, *args, **kwargs):
        # overrites default delete function to handle card_count decrease
        if self.board.card_count > 0:
            self.board.card_count -= 1
            self.board.save()
        super().delete(*args, **kwargs)