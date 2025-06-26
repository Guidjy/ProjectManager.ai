from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views
from .views import (ProjectViewSet, MemberViewSet, RoleViewSet, ProjectCharterViewSet,
    WorkBreakdownStructureViewSet, ReportViewSet, KanbanBoardViewSet, KanbanCardViewSet,)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'project-charters', ProjectCharterViewSet)
router.register(r'work-breakdown-structures', WorkBreakdownStructureViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'kanban-boards', KanbanBoardViewSet)
router.register(r'kanban-cards', KanbanCardViewSet)


urlpatterns = [
    path('', views.test),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)