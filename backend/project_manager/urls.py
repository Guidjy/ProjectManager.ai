from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views
from .views import (ProjectViewSet, MemberViewSet, RoleViewSet, ProjectCharterViewSet,
    WorkBreakdownStructureViewSet, StatusReportViewSet, KanbanBoardViewSet, KanbanCardViewSet,)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'project-charters', ProjectCharterViewSet)
router.register(r'work-breakdown-structures', WorkBreakdownStructureViewSet)
router.register(r'status-reports', StatusReportViewSet)
router.register(r'kanban-boards', KanbanBoardViewSet)
router.register(r'kanban-cards', KanbanCardViewSet)


urlpatterns = [
    path('', views.test),
    path('', include(router.urls)),
    path('generate-report/<int:project_id>/', views.generate_report),
    path('generate-kanban-board/<int:project_id>', views.generate_kanban_board),
    path('ask-ai/', views.ask_ai),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)