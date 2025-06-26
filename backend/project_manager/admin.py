from django.contrib import admin
from .models import Project, Member, Role, ProjectCharter, WorkBreakdownStructure, Report, KanbanBoard, KanbanCard


admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Role)
admin.site.register(ProjectCharter)
admin.site.register(WorkBreakdownStructure)
admin.site.register(Report)
admin.site.register(KanbanBoard)
admin.site.register(KanbanCard)
